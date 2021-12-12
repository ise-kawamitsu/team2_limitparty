from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

######### アプリ Top View ##########
def title(request):
    """ アプリ Top Page """
    return render(request, 'title.html')

def top(request):
    """ アプリ 選択画面 """
    return render(request, 'top.html')

######### 無料ver View ##########
def index(request):
    """ 無料版 Top Page """
    return render(request, 'freeverapp/index.html')

######### 有料ver View ##########
def signup(request):
    """ 有料会員登録ページ """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username = username)
            return render(request, 'paidverapp/signup.html', {'error' : 'この名前は登録済みです'}) 
        except:
            user = User.objects.create_user(username, '', password)
            return render(request, 'paidverapp/signup.html', {'done':'有料会員登録完了しました'})
    return render(request, 'paidverapp/signup.html')

def signin(request):
    """ ログインページ """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        
        if username =='admin':
            print("hello")
            return redirect('articles_admin')
        elif user is not None:
            login(request, user)
            return redirect('p_top')
        else:
            context = {
                'alert' : '正しいユーザー名,パスワードを入力して下さい。',
            }
            return render(request, 'paidverapp/login.html', context)
    return render(request, 'paidverapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('paidverapp/login')


# @login_required
def ptop(request):
    """ 有料版 Top Page """
    return render(request, 'paidverapp/top.html')


######### GAME View ##########
QNUM = 0
def f_quiz(request):
    """
        無料版なぞなぞゲーム
        問題数10
    """
    global QNUM
    q = [
        '「海」「魚」「海藻」のうち、愛があるのはどれでしょうか？',
        'お酒は20才、タバコも20才、車に乗れるのは何才から？',
        '奈良の大仏と鎌倉の大仏は、どちらが先にたったでしょう？',
        '笑っている人しかいないお店は？',
        '''国際会議の最中に突然停電になりました。
        一番初めに「電気を付けろ！」と叫んだのは、
        どこの国の人でしょう？''',
        '春、夏、秋、冬、一年の中で最も長い日数はどれ?',
        '「新聞紙」を上から読むと「しんぶんし」、下から読むと?',
        '''
        ライオンが5mの鎖に繋がれている。
        ライオンは自分の周囲、何mの草を食べる事ができる?
        ''',
        ' 英語のアルファベットの一番最初の文字はA。Aは、Bの前にある。では、一番最後の文字は何？',
        '「ゾウ」「ウシ」「ワニ」のうち、蚊に刺された動物はどれでしょうか？',
    ]

    answers = [
        '魚 「愛がある＝Eyeがある」→「目がある」→『魚』',
        '0歳（誰でも乗ることはできるから）',
        'どちらも立ってなく座ってます。',
        'クスリ屋さん',
        '日本 「電気を付けろ！」と日本語で言っている',
        '一年（選択肢・春、夏、秋、冬、一年）',
        'よみにくい',
        '0m。（ライオンは草を食べない）',
        'A,「T」（ALPHABET）',
        '「ウシ」 「ウシ＝家畜」→「かちく」→『蚊、チクッ！』！',
    ]
    try:
        quiz = q[QNUM]
        ans = answers[QNUM]
        QNUM += 1
        context = {'qnum': QNUM, 'quiz' : quiz, 'ans': ans}

        return render(request, 'game/freequiz.html', context)
    except (IndexError, UnboundLocalError):
        QNUM = 0
        context = {'quiz' : '終了です'}
        return render(request, 'game/freequiz.html', context)


PNUM = 0
def p_quiz(request):
    """
        有料版なぞなぞゲーム
        問題数20
    """
    global PNUM
    q = [
        '「海」「魚」「海藻」のうち、愛があるのはどれでしょうか？',
        'お酒は20才、タバコも20才、車に乗れるのは何才から？',
        '奈良の大仏と鎌倉の大仏は、どちらが先にたったでしょう？',
        '笑っている人しかいないお店は？',
        '''国際会議の最中に突然停電になりました。
        一番初めに「電気を付けろ！」と叫んだのは、
        どこの国の人でしょう？''',
        '春、夏、秋、冬、一年の中で最も長い日数はどれ?',
        '「新聞紙」を上から読むと「しんぶんし」、下から読むと?',
        '''
        ライオンが5mの鎖に繋がれている。
        ライオンは自分の周囲、何mの草を食べる事ができる?
        ''',
        ' 英語のアルファベットの一番最初の文字はA。Aは、Bの前にある。では、一番最後の文字は何？',
        '「ゾウ」「ウシ」「ワニ」のうち、蚊に刺された動物はどれでしょうか？',
        'testtesttesttest1',
        'testtesttesttest2',
    ]

    answers = [
        '魚 「愛がある＝Eyeがある」→「目がある」→『魚』',
        '0歳（誰でも乗ることはできるから）',
        'どちらも立ってなく座ってます。',
        'クスリ屋さん',
        '日本 「電気を付けろ！」と日本語で言っている',
        '一年（選択肢・春、夏、秋、冬、一年）',
        'よみにくい',
        '0m。（ライオンは草を食べない）',
        'A,「T」（ALPHABET）',
        '「ウシ」 「ウシ＝家畜」→「かちく」→『蚊、チクッ！』！',
        'testtesttesttest1',
        'testtesttesttest2',
    ]
    try:
        quiz = q[PNUM]
        ans = answers[PNUM]
        PNUM += 1
        context = {'qnum': PNUM, 'quiz' : quiz, 'ans': ans}

        return render(request, 'game/paidquiz.html', context)
    except (IndexError, UnboundLocalError):
        PNUM = 0
        context = {'quiz' : '終了です'}
        return render(request, 'game/paidquiz.html', context)


