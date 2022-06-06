from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    """新しいユーザーを登録する"""
    if request.method != 'POST':
        # データは送信されていないので空のフォームを生成する
        form = UserCreationForm()
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # ユーザーをログインさせてホームページにリダイレクトする
            login(request, new_user)
            return redirect('learning_logs:index')

    # 空または無効のフォームを表示する
    context = {'form': form}
    return render(request, 'registration/register.html', context)

