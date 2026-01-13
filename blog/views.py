from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View

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
        'tg_link': 'https://t.me/c/2828107333/11/1352'
    },
    {
        'id': 2,
        'title': 'Erondagi namoyishlar: xaritalar ustida sharh',
        'slug': 'erondagi-namoyishlar-xaritalar-ustida-sharh',
        'published_date': datetime(2026, 1, 11, 10, 2),
        'views': 31927,
        'reading_minute': 10,
        'content': '''Hozirda 31 ta viloyatdan 30 tasida namoyishlar kuzatilmoqda. Ular orasida ayniqsa Mashhad shahri alohida e’tiborga loyiq. Mashhad Tehrondan keyin aholi soni bo‘yicha ikkinchi eng yirik shahar bo‘lib, mamlakatning muhim iqtisodiy salohiyatini ta’minlaydi. Eron oliy rahbari Xominaiy aynan Mashhadda tug‘ilgan. Shahar Eron Islom Respublikasining ma’naviy tayanchi hisoblanadi, chunki bu yerda Imom Rizo majmuasi va ko‘plab diniy markazlar joylashgan. So‘nggi kunlarda ijtimoiy tarmoqlarda Mashhadda 30 metrli Eron bayrog‘i yirtib tashlangani va oyatullohga qarshi keskin shiorlar yangragani aks etgan videolar tarqaldi. Bu holat Eron rejimidan nafaqat dunyoviy qatlam, balki diniy va konservativ guruhlar ham norozilik bildirayotganini ko‘rsatadi.''',
        'tg_link': 'https://t.me/c/2828107333/11/1329'
    },
]


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'home.html')


class BlogsView(View):
    pass


class BlogDetailView(View):
    pass
