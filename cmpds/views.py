from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
from cmpds.models import Compound

from django.views.generic import CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse_lazy

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# import chemspipy?

# Create your views here.


@login_required
def index(request):
    t = loader.get_template('cmpds/cmpdsindex.html')
    allCompounds = Compound.objects.all()
    paginator = Paginator(allCompounds, 10)
    page = request.GET.get('page')
    try:
        compounds = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        compounds = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        compounds = paginator.page(paginator.num_pages)
    C = Context({'compounds': compounds})
    return HttpResponse(t.render(C))


class cmpdCreateView(CreateView):
    model = Compound
    fields = [
        'chemName', 'SMILES', 'InCHI', 'CSID', 'box', 'row', 'column', 'vendor',
        'vendorCatNo', 'solvent', 'solventNote', 'molecularWeight', 'concmM',
        'reasonOrdered', 'personOrdered', 'powderLocation', 'mechanismTargetNotes',
        'note', 'rothID', 'dateOrdered', 'libraryCode'
    ]
    success_url = '/cmpds/'

    # def get_object(self):
    #     return get_object_or_404(compound, pk=request.session['pk'])

    # def get_success_url(self):
    # return reverse_lazy('cmpd-detail', kwargs={'pk':
    # get_object_or_404().id})


class cmpdUpdateView(UpdateView):
    model = Compound
    template_name_suffix = '_update_form'
    fields = [
        'chemName', 'SMILES', 'InCHI', 'CSID', 'box', 'row', 'column', 'vendor',
        'vendorCatNo', 'solvent', 'solventNote', 'molecularWeight', 'concmM',
        'reasonOrdered', 'personOrdered', 'powderLocation', 'mechanismTargetNotes',
        'note', 'rothID', 'dateOrdered', 'libraryCode'
    ]
    success_url = '/cmpds/'
    # def get_success_url(self):
    #   return reverse_lazy('cmpd-detail',kwargs={'pk': self.get_object().id})


class cmpdDeleteView(DeleteView):
    model = Compound
    success_url = '/cmpds/'
    # def get_success_url(self):
    #   return reverse_lazy('cmpd-list')


@login_required
def cmpdDetail(request, pk):
    t = loader.get_template('cmpds/cmpddetail.html')
    thiscmpd = Compound.objects.get(pk=pk)
    # chemspider url
    C = Context({
        'cmpd': thiscmpd,
        # chemspider info here
    })
    return HttpResponse(t.render(C))


@login_required
def cmpdCSV(request):
    import csv
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="DMSOStocks.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'chemName', 'SMILES', 'InCHI', 'CSID', 'box', 'row', 'column', 'vendor',
        'vendorCatNo', 'solvent', 'solventNote', 'molecularWeight', 'concmM',
        'reasonOrdered', 'personOrdered', 'powderLocation', 'mechanismTargetNotes',
        'note', 'rothID', 'dateOrdered', 'libraryCode'
    ])
    for cmpd in Compound.objects.all():
        writer.writerow([
            cmpd.chemName, cmpd.SMILES, cmpd.InCHI, cmpd.CSID, cmpd.box, cmpd.row,
            cmpd.column, cmpd.vendor, cmpd.vendorCatNo, cmpd.solvent,
            cmpd.solventNote, cmpd.molecularWeight, cmpd.concmM, cmpd.reasonOrdered,
            cmpd.personOrdered, cmpd.powderLocation, cmpd.mechanismTargetNotes,
            cmpd.note, cmpd.dateOrdered, cmpd.libraryCode
        ])

    return response
