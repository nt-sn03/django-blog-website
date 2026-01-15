from datetime import datetime
from uuid import uuid4

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.text import slugify

from .forms import BlogCreateForm, BlogSearchForm

posts: list[dict] = [
    {
        'id': 1,
        'title': 'Erondagi namoyishlar: hozirgacha nimalar ma’lum?',
        'slug': 'erondagi-namoyishlar-hozirgacha-nimalar-malum',
        'published_date': datetime(2026, 1, 10, 7, 32),
        'views': 45927,
        'reading_minute': 8,
        'content': '''Guvohlar tomonidan olingan videolarda rasmiylarning namoyishlarni bostirishdagi harakatlari yanada shafqatsiz tus olayotganini ko‘rsatmoqda.

                    Xalqaro axborot agentliklari voqealarni Eron hududida turib yoritish imkoniga ega emas. Bundan tashqari, mamlakat rasmiylari payshanba kuni internetni to‘liq o‘chirib qo‘ygan va bu ma’lumot yig‘ish va tekshirishni yanada qiyinlashtirgan.

                    Shunga qaramay, OAV ixtiyoriga mamlakatdan ayrim videoyozuvlar yetib kelmoqda, jurnalistlar Eronda bo‘lib turgan va voqealarni to‘g‘ridan to‘g‘ri kuzatish imkoniga ega bo‘lgan odamlar bilan bog‘lanmoqda.

                    Shanba kuni olingan videolardan birida namoyishchilar Tehronning Gisha tumanidagi ko‘chalarni nazorat qilayotgani aks etgan. Ayrim videoroliklarda esa Eronning ikkinchi eng yirik shahri bo‘lmish Mashhadda namoyishchilar xavfsizlik kuchlari bilan to‘qnashganini ko‘rish mumkin.
        ''',
        'tg_link': 'https://t.me/c/2828107333/11/1352',
        'is_published': True
    },
    {
        'id': 2,
        'title': 'Erondagi namoyishlar: xaritalar ustida sharh',
        'slug': 'erondagi-namoyishlar-xaritalar-ustida-sharh',
        'published_date': datetime(2026, 1, 11, 10, 2),
        'views': 31927,
        'reading_minute': 10,
        'content': '''Hozirda 31 ta viloyatdan 30 tasida namoyishlar kuzatilmoqda. Ular orasida ayniqsa Mashhad shahri alohida e’tiborga loyiq. Mashhad Tehrondan keyin aholi soni bo‘yicha ikkinchi eng yirik shahar bo‘lib, mamlakatning muhim iqtisodiy salohiyatini ta’minlaydi. Eron oliy rahbari Xominaiy aynan Mashhadda tug‘ilgan. Shahar Eron Islom Respublikasining ma’naviy tayanchi hisoblanadi, chunki bu yerda Imom Rizo majmuasi va ko‘plab diniy markazlar joylashgan. So‘nggi kunlarda ijtimoiy tarmoqlarda Mashhadda 30 metrli Eron bayrog‘i yirtib tashlangani va oyatullohga qarshi keskin shiorlar yangragani aks etgan videolar tarqaldi. Bu holat Eron rejimidan nafaqat dunyoviy qatlam, balki diniy va konservativ guruhlar ham norozilik bildirayotganini ko‘rsatadi.''',
        'tg_link': 'https://t.me/c/2828107333/11/1329',
        'is_published': True
    },
]


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'home.html', {'posts': posts[-2:]})


class BlogsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.GET:
            form = BlogSearchForm(request.GET)
            if form.is_valid():
                search = form.cleaned_data['search']

                result = []
                for post in posts:
                    if search.lower() in post['title'].lower():
                        result.append(post)

                return render(request, 'blog.html', {'posts': result, 'search': search})

        return render(request, 'blog.html', {'posts': posts[::-1]})


class BlogDetailView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        for post in posts:
            if post['slug'] == slug:
                post['views'] += 1
                return render(request, 'blog_detail.html', {'post': post})
        return render(request, 'blog.html', {'posts': posts, 'error': f'{slug} is not found.'})


class BlogCreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = BlogCreateForm()
        return render(request, 'blog_create.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = BlogCreateForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            
            data['id'] = str(uuid4())
            data['slug'] = slugify(data['title'])
            data['views'] = 0
            data['published_date'] = datetime.now()

            posts.append(data)
            return redirect(reverse('blogs'))
        
        return render(request, 'blog_create.html', {'form': form})
