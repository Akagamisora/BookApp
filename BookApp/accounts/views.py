from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user  # ログインユーザーを所有者に設定
            book.save()
            return redirect('book_list')  # 書籍一覧ページにリダイレクト
    else:
        form = BookForm()
    return render(request, 'accounts/add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.filter(owner=request.user)
    return render(request, 'accounts/book_list.html', {'books': books})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, owner=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'accounts/edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, owner=request.user)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'accounts/delete_book.html', {'book': book})