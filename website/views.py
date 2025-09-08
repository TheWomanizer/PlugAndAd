from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html')


def pricing(request):
    pricing_plans = [
        {
            'name': 'Starter',
            'price': 29,
            'period': '/mes',
            'description': 'Perfecto para pequeñas empresas que empiezan con ads',
            'features': [
                'Hasta 3 cuentas publicitarias',
                'Optimización automática básica',
                'Reportes semanales',
                'Soporte por email',
                'Dashboard básico',
            ],
            'cta': 'Comenzar gratis',
            'popular': False,
        },
        {
            'name': 'Professional',
            'price': 99,
            'period': '/mes',
            'description': 'Para empresas que buscan maximizar su ROAS',
            'features': [
                'Hasta 10 cuentas publicitarias',
                'Optimización con IA avanzada',
                'Reportes diarios personalizados',
                'Soporte prioritario 24/7',
                'Dashboard avanzado con insights',
                'Integración con herramientas CRM',
            ],
            'cta': 'Prueba gratuita 14 días',
            'popular': True,
        },
        {
            'name': 'Enterprise',
            'price': 299,
            'period': '/mes',
            'description': 'Solución completa para grandes equipos',
            'features': [
                'Cuentas publicitarias ilimitadas',
                'IA personalizada para tu industria',
                'Reportes en tiempo real',
                'Account Manager dedicado',
                'Dashboard white-label',
                'API personalizada',
                'Integración completa con tu stack',
            ],
            'cta': 'Contactar ventas',
            'popular': False,
        },
    ]
    
    return render(request, 'website/pricing.html', {
        'pricing_plans': pricing_plans
    })


def signup(request):
    return render(request, 'website/signup.html')


def packages(request):
    return render(request, 'website/packages.html')


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
            'bio': 'Líder visionario con experiencia en publicidad digital y desarrollo de productos tecnológicos.',
            'linkedin': '#'
        },
        {
            'name': 'Miguel José Villegas',
            'role': 'Co-Fundador',
            'image': '👨‍💻',
            'bio': 'Experto en desarrollo y arquitectura de sistemas publicitarios automatizados.',
            'linkedin': '#'
        },
        {
            'name': 'María Fernanda Álvarez',
            'role': 'Head of Operations',
            'image': '👩‍💼',
            'bio': 'Especialista en optimización de procesos y gestión de campañas publicitarias.',
            'linkedin': '#'
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
