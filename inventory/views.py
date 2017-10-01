from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from django.views.generic.base import View

from inventory.forms import ItemForm1, ItemForm2, ItemForm3
from inventory.models import Item


# this is old method
# -------------------------------------------------

# def index(request):
#     # items=Item.objects.exclude(amount=0)
#     items = Item.objects.all()
#     return render(request, 'inventory/index.html',
#                   {'items': items}
#                   )


# def item_details(request, id):
#     try:
#         item = Item.objects.get(id=id)
#     except Item.DoesNotExist:
#         raise Http404('This item does not exist')
#     return render(request, 'inventory/item_details.html',
#                   {'item': item}
#                   )


# try this
# ----------------------------------------------


class IndexView(View):
    template_name = 'inventory/index.html'

    def get(self,request):
        items = Item.objects.all()
        return render(request,
                      self.template_name,
                      {'items': items})

    def post(self,request):
        amount = int(request.POST['amount'])
        items = Item.objects.filter(amount__lte=amount)
        return render(request,
                      self.template_name,
                      {'items': items})


class ItemDetailsView(View):
    template_name = 'inventory/item_details.html'

    def get(self, request, id):
        # try:
        #     item = Item.objects.get(id=id)
        # except Item.DoesNotExist:
        #     raise Http404('This item does not exist')

        # convert all three lines into one
        item = get_object_or_404(Item,id=id)
        return render(request,
                      self.template_name,
                      {'item': item})


# for add an item

class ItemAdd1View(View):
    template_name = 'inventory/add_item_1.html'

    def get(self, request):
        form = ItemForm1()
        return render(request,
                      self.template_name,
                      {'form': form})

    def post(self,request):
        form = ItemForm1(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))

class ItemAdd2View(View):
    template_name = 'inventory/add_item_2.html'

    def get(self, request):
        form = ItemForm2()
        return render(request,
                      self.template_name,
                      {'form': form})

    def post(self,request):
        form = ItemForm2(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))

class ItemAdd3View(View):
    template_name = 'inventory/add_item_3.html'

    def get(self, request):
        form = ItemForm3()
        return render(request,
                      self.template_name,
                      {'form': form})

    def post(self,request):
        form = ItemForm3(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))


# manual add
class ItemAdd4View(View):
    template_name = 'inventory/add_item_4.html'

    def get(self, request):
        return render(request,
                      self.template_name)

    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        amount = request.POST['amount']
        Item(title=title,description=description,amount=amount).save()
        return HttpResponseRedirect(reverse('index'))


