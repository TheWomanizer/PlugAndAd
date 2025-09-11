from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html')


def pricing(request):
    pricing_plans = [
        {
            'name': 'Starter',
            'price': 29,
            'period': '/mes',
            'description': 'Para empezar con Ads multicanal',
            'features': [
                'Hasta 2 cuentas publicitarias conectadas',
                '1 espacio de trabajo / 2 usuarios',
                'Reglas básicas y recomendaciones iniciales',
                'Reportes semanales (email + dashboard)',
                'Soporte por email (24–48 h)',
            ],
            'cta': 'Comenzar gratis',
            'popular': False,
        },
        {
            'name': 'Professional',
            'price': 99,
            'period': '/mes',
            'description': 'Para equipos que optimizan a diario',
            'features': [
                'Hasta 10 cuentas publicitarias conectadas',
                '3 espacios / 5 usuarios',
                'Reglas avanzadas + alertas',
                'Recomendaciones con IA (beta)',
                'Reportes diarios y exportación CSV',
                'Integraciones: Slack / Looker Studio (conector)',
                'Soporte prioritario en horario laboral (COT)',
            ],
            'cta': 'Prueba gratuita 14 días',
            'popular': True,
        },
        {
            'name': 'Enterprise',
            'price': 299,
            'period': '/mes',
            'description': 'Para operaciones multi-marca/país',
            'features': [
                'Límite de cuentas a medida',
                'SSO (SAML/OIDC) y roles avanzados',
                'API de lectura/escritura y webhooks',
                'Acompañamiento de onboarding',
                'Acuerdos de seguridad y DPA',
                'Soporte dedicado y canal privado',
            ],
            'cta': 'Contactar ventas',
            'popular': False,
        },
    ]
    
    # Si el usuario está autenticado, usar template de dashboard
    if request.user.is_authenticated:
        return render(request, 'auth_app/pricing.html', {
            'pricing_plans': pricing_plans
        })
    else:
        return render(request, 'website/pricing.html', {
            'pricing_plans': pricing_plans
        })


def signup(request):
    return render(request, 'website/signup.html')


def packages(request):
    # Solo permitir acceso a usuarios autenticados
    if request.user.is_authenticated:
        return render(request, 'auth_app/packages.html')
    else:
        return render(request, 'website/home.html')


# About section views
def about(request):
    return render(request, 'website/about/about.html')


def about_mission(request):
    return render(request, 'website/about/mission.html')


def about_team(request):
    team_members = [
        {
            'name': 'José Alejandro Jiménez Vásquez',
            'role': 'CEO & Fundador',
            'image': '👨‍💼',
            'bio': 'Producto y growth. Construyendo Plug&Ad para hacer el marketing más simple y medible.',
            'linkedin': 'https://www.linkedin.com/in/jose-jimenez-vasquez-a388571a2/',
            'github': 'https://github.com/TheWomanizer'
        },
        {
            'name': 'Miguel José Villegas',
            'role': 'Co-Fundador',
            'image': '👨‍💻',
            'bio': 'Experto en desarrollo y arquitectura de sistemas publicitarios automatizados.',
            'linkedin': '#',
            'github': 'https://github.com/ll333ll'
        },
        {
            'name': 'María Fernanda Álvarez',
            'role': 'Head of Operations',
            'image': '👩‍💼',
            'bio': 'Especialista en optimización de procesos y gestión de campañas publicitarias.',
            'linkedin': '#',
            'github': 'https://github.com/ll333ll'
        }
    ]
    
    return render(request, 'website/about/team.html', {
        'team_members': team_members
    })


def about_privacy(request):
    return render(request, 'website/about/privacy.html')


def about_terms(request):
    return render(request, 'website/about/terms.html')


def about_contact(request):
    return render(request, 'website/about/contact.html')
