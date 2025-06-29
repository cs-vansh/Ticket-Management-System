from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tickets.models import Ticket
from django.utils import timezone
from django.db.models.functions import TruncMonth
from django.db.models import Count


@login_required
def dashboard(request):
    
    #Pie chart data
    active_count = Ticket.objects.filter(ticket_status='Active').count()
    pending_count = Ticket.objects.filter(ticket_status='Pending').count()
    completed_count = Ticket.objects.filter(ticket_status='Completed').count()

    pie_data = {
        'labels': ['Active', 'Pending', 'Completed'],
        'values': [active_count, pending_count, completed_count],
    }

    # Bar chart data
    today = timezone.now()
    six_months_ago = today - timezone.timedelta(days=6*30)
    tickets_resolved = Ticket.objects.filter(
        ticket_status='Completed',
        closed_date__gte=six_months_ago
    ).annotate(month=TruncMonth('closed_date')).values('month').annotate(count=Count('id')).order_by('month')

    bar_labels = []
    bar_values = []
    for ticket in tickets_resolved:
        bar_labels.append(ticket['month'].strftime('%B %Y'))
        bar_values.append(ticket['count'])

    bar_data = {
        'labels': bar_labels,
        'values': bar_values,
    }

    context = {'pie_data': pie_data, 'bar_data':bar_data}

    return render(request, 'dashboard/dashboard.html', context)
