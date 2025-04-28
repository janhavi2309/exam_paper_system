from django.shortcuts import render, redirect
from .models import Paper, DecryptionRequest, ModerationReview, FinalSelection
from .encryption_utils import encrypt_file, decrypt_file
from users.models import CustomUser
from django.core.files.base import ContentFile
from django.http import HttpResponse
import random

# Teacher uploading paper
def upload_paper(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        file_data = file.read()
        encrypted_file_data, key = encrypt_file(file_data)

        paper = Paper(
            teacher=request.user,
            encrypted_key=key,
        )
        paper.file.save(file.name, ContentFile(encrypted_file_data))
        paper.save()
        return redirect('teacher_dashboard')

    return render(request, 'papers/upload_paper.html')

# Moderator viewing and requesting decryption
def moderator_dashboard(request):
    papers = Paper.objects.all()
    return render(request, 'papers/moderator_dashboard.html', {'papers': papers})

def request_decryption(request, paper_id):
    paper = Paper.objects.get(id=paper_id)
    DecryptionRequest.objects.create(paper=paper, moderator=request.user)
    return redirect('moderator_dashboard')

# Admin approving decryption
def admin_dashboard(request):
    requests = DecryptionRequest.objects.filter(status='Pending')
    return render(request, 'papers/admin_dashboard.html', {'requests': requests})

def approve_decryption(request, request_id):
    req = DecryptionRequest.objects.get(id=request_id)
    req.status = 'Approved'
    req.save()
    return redirect('admin_dashboard')

def reject_decryption(request, request_id):
    req = DecryptionRequest.objects.get(id=request_id)
    req.status = 'Rejected'
    req.save()
    return redirect('admin_dashboard')

# Moderator viewing decrypted paper
def view_decrypted_paper(request, paper_id):
    paper = Paper.objects.get(id=paper_id)
    with open(paper.file.path, 'rb') as f:
        enc_data = f.read()
    file_data = decrypt_file(enc_data, paper.encrypted_key)
    return HttpResponse(file_data, content_type='application/pdf')

# Moderator approving/rejecting papers
def review_paper(request, paper_id):
    paper = Paper.objects.get(id=paper_id)
    if request.method == 'POST':
        decision = request.POST['decision']
        ModerationReview.objects.create(
            paper=paper,
            moderator=request.user,
            decision=decision
        )
        paper.status = 'Approved' if decision == 'Approved' else 'Rejected'
        paper.save()
        return redirect('moderator_dashboard')
    return render(request, 'papers/review_paper.html', {'paper': paper})

# Admin random selection
def final_selection(request):
    papers = Paper.objects.filter(status='Approved')
    selected_paper = random.choice(papers)
    FinalSelection.objects.create(paper=selected_paper)
    return HttpResponse(f"Selected Paper ID: {selected_paper.id}")

