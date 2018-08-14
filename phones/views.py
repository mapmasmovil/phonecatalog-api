from django.http import JsonResponse


def phones(request):
    return JsonResponse({
        'page': 0,
        'before': 0,
        'after': 0,
        'phones': [
            {
                'id': 1,
                'title': 'Nexus 5X',
                'description': 'Android smartphone manufactured by LG Electronics, co-developed with and marketed by Google Inc., as apart of its Nexus line of flagship devices.',
                'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Nexus_5X_%28White%29.jpg/640px-Nexus_5X_%28White%29.jpg',
                'colors': ['carbon', 'quartz', 'ice'],
                'storage': ['16GB', '32GB'],
                'cpu': '1.8GHz hexa core',
                'battery': '2700 mAh Li-Po',
                'released': 2015,
                'os': 'Android',
            },
            {
                'id': 2,
                'title': 'iPhone X',
                'description': 'It\'s a smartphone designed, developed, and marketed by Apple Inc. This device marks the iPhone series\' tenth anniversary',
                'image': 'https://www.t-mobile.com/content/dam/t-mobile/en-p/cell-phones/apple/apple-iphone-x/silver/Apple-iPhoneX-Silver-1-3x.jpg',
                'colors': ['silver', 'space grey'],
                'storage': ['64GB', '256GB'],
                'cpu': '2.39GHz hexa core',
                'battery': '2716 mAh Li-ion',
                'released': 2017,
                'os': 'iOS',
            },

        ]
    })
