from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse, reverse_lazy
from hammer.mixins import AJAXResponseMixin
from hammerdemo.models import (
    
    DemoPersonSiblings,
    
    DemoPerson,
    
    DemoPersonParents,
    
    DemoFamilyPets,
    
    DemoFamily,
    
    DemoFamilyMembers,
    
    DemoPet,
    
    DemoPersonChildren,
    
)


class DemopersonsiblingsListView(ListView, AJAXResponseMixin):
    model = DemoPersonSiblings
    template_name = 'demopersonsiblings_list.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list = self.object_list)
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        res_format = request.GET.get('format')
        if res_format and res_format.lower() in 'json':
            return self.render_obj_to_json(context)
        if res_format and res_format.lower() in 'xml':
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemopersonsiblingsCreateView(CreateView):
    model = DemoPersonSiblings
    success_url = reverse_lazy('demopersonsiblings_list')
    template_name = 'demopersonsiblings_create.html'


class DemopersonsiblingsDetailView(DetailView, AJAXResponseMixin):
    model = DemoPersonSiblings
    template_name = 'demopersonsiblings_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        res_format = request.GET.get('format')
        if res_format and 'json' in res_format.lower():
            return self.render_obj_to_json(context)
        if res_format and 'xml' in res_format.lower():
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemopersonsiblingsUpdateView(UpdateView):
    model = DemoPersonSiblings
    success_url = reverse_lazy('demopersonsiblings_list')
    template_name = 'demopersonsiblings_update.html'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)


class DemopersonsiblingsDeleteView(DeleteView):
    model = DemoPersonSiblings
    success_url = reverse_lazy('demopersonsiblings_list')
    template_name = 'demopersonsiblings_confirm_delete.html'


class DemopersonListView(ListView, AJAXResponseMixin):
    model = DemoPerson
    template_name = 'demoperson_list.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list = self.object_list)
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        res_format = request.GET.get('format')
        if res_format and res_format.lower() in 'json':
            return self.render_obj_to_json(context)
        if res_format and res_format.lower() in 'xml':
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemopersonCreateView(CreateView):
    model = DemoPerson
    success_url = reverse_lazy('demoperson_list')
    template_name = 'demoperson_create.html'


class DemopersonDetailView(DetailView, AJAXResponseMixin):
    model = DemoPerson
    template_name = 'demoperson_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        res_format = request.GET.get('format')
        if res_format and 'json' in res_format.lower():
            return self.render_obj_to_json(context)
        if res_format and 'xml' in res_format.lower():
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemopersonUpdateView(UpdateView):
    model = DemoPerson
    success_url = reverse_lazy('demoperson_list')
    template_name = 'demoperson_update.html'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)


class DemopersonDeleteView(DeleteView):
    model = DemoPerson
    success_url = reverse_lazy('demoperson_list')
    template_name = 'demoperson_confirm_delete.html'


class DemopersonparentsListView(ListView, AJAXResponseMixin):
    model = DemoPersonParents
    template_name = 'demopersonparents_list.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list = self.object_list)
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        res_format = request.GET.get('format')
        if res_format and res_format.lower() in 'json':
            return self.render_obj_to_json(context)
        if res_format and res_format.lower() in 'xml':
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemopersonparentsCreateView(CreateView):
    model = DemoPersonParents
    success_url = reverse_lazy('demopersonparents_list')
    template_name = 'demopersonparents_create.html'


class DemopersonparentsDetailView(DetailView, AJAXResponseMixin):
    model = DemoPersonParents
    template_name = 'demopersonparents_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        res_format = request.GET.get('format')
        if res_format and 'json' in res_format.lower():
            return self.render_obj_to_json(context)
        if res_format and 'xml' in res_format.lower():
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemopersonparentsUpdateView(UpdateView):
    model = DemoPersonParents
    success_url = reverse_lazy('demopersonparents_list')
    template_name = 'demopersonparents_update.html'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)


class DemopersonparentsDeleteView(DeleteView):
    model = DemoPersonParents
    success_url = reverse_lazy('demopersonparents_list')
    template_name = 'demopersonparents_confirm_delete.html'


class DemofamilypetsListView(ListView, AJAXResponseMixin):
    model = DemoFamilyPets
    template_name = 'demofamilypets_list.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list = self.object_list)
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        res_format = request.GET.get('format')
        if res_format and res_format.lower() in 'json':
            return self.render_obj_to_json(context)
        if res_format and res_format.lower() in 'xml':
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemofamilypetsCreateView(CreateView):
    model = DemoFamilyPets
    success_url = reverse_lazy('demofamilypets_list')
    template_name = 'demofamilypets_create.html'


class DemofamilypetsDetailView(DetailView, AJAXResponseMixin):
    model = DemoFamilyPets
    template_name = 'demofamilypets_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        res_format = request.GET.get('format')
        if res_format and 'json' in res_format.lower():
            return self.render_obj_to_json(context)
        if res_format and 'xml' in res_format.lower():
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemofamilypetsUpdateView(UpdateView):
    model = DemoFamilyPets
    success_url = reverse_lazy('demofamilypets_list')
    template_name = 'demofamilypets_update.html'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)


class DemofamilypetsDeleteView(DeleteView):
    model = DemoFamilyPets
    success_url = reverse_lazy('demofamilypets_list')
    template_name = 'demofamilypets_confirm_delete.html'


class DemofamilyListView(ListView, AJAXResponseMixin):
    model = DemoFamily
    template_name = 'demofamily_list.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list = self.object_list)
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        res_format = request.GET.get('format')
        if res_format and res_format.lower() in 'json':
            return self.render_obj_to_json(context)
        if res_format and res_format.lower() in 'xml':
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemofamilyCreateView(CreateView):
    model = DemoFamily
    success_url = reverse_lazy('demofamily_list')
    template_name = 'demofamily_create.html'


class DemofamilyDetailView(DetailView, AJAXResponseMixin):
    model = DemoFamily
    template_name = 'demofamily_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        res_format = request.GET.get('format')
        if res_format and 'json' in res_format.lower():
            return self.render_obj_to_json(context)
        if res_format and 'xml' in res_format.lower():
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemofamilyUpdateView(UpdateView):
    model = DemoFamily
    success_url = reverse_lazy('demofamily_list')
    template_name = 'demofamily_update.html'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)


class DemofamilyDeleteView(DeleteView):
    model = DemoFamily
    success_url = reverse_lazy('demofamily_list')
    template_name = 'demofamily_confirm_delete.html'


class DemofamilymembersListView(ListView, AJAXResponseMixin):
    model = DemoFamilyMembers
    template_name = 'demofamilymembers_list.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list = self.object_list)
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        res_format = request.GET.get('format')
        if res_format and res_format.lower() in 'json':
            return self.render_obj_to_json(context)
        if res_format and res_format.lower() in 'xml':
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemofamilymembersCreateView(CreateView):
    model = DemoFamilyMembers
    success_url = reverse_lazy('demofamilymembers_list')
    template_name = 'demofamilymembers_create.html'


class DemofamilymembersDetailView(DetailView, AJAXResponseMixin):
    model = DemoFamilyMembers
    template_name = 'demofamilymembers_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        res_format = request.GET.get('format')
        if res_format and 'json' in res_format.lower():
            return self.render_obj_to_json(context)
        if res_format and 'xml' in res_format.lower():
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemofamilymembersUpdateView(UpdateView):
    model = DemoFamilyMembers
    success_url = reverse_lazy('demofamilymembers_list')
    template_name = 'demofamilymembers_update.html'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)


class DemofamilymembersDeleteView(DeleteView):
    model = DemoFamilyMembers
    success_url = reverse_lazy('demofamilymembers_list')
    template_name = 'demofamilymembers_confirm_delete.html'


class DemopetListView(ListView, AJAXResponseMixin):
    model = DemoPet
    template_name = 'demopet_list.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list = self.object_list)
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        res_format = request.GET.get('format')
        if res_format and res_format.lower() in 'json':
            return self.render_obj_to_json(context)
        if res_format and res_format.lower() in 'xml':
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemopetCreateView(CreateView):
    model = DemoPet
    success_url = reverse_lazy('demopet_list')
    template_name = 'demopet_create.html'


class DemopetDetailView(DetailView, AJAXResponseMixin):
    model = DemoPet
    template_name = 'demopet_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        res_format = request.GET.get('format')
        if res_format and 'json' in res_format.lower():
            return self.render_obj_to_json(context)
        if res_format and 'xml' in res_format.lower():
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemopetUpdateView(UpdateView):
    model = DemoPet
    success_url = reverse_lazy('demopet_list')
    template_name = 'demopet_update.html'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)


class DemopetDeleteView(DeleteView):
    model = DemoPet
    success_url = reverse_lazy('demopet_list')
    template_name = 'demopet_confirm_delete.html'


class DemopersonchildrenListView(ListView, AJAXResponseMixin):
    model = DemoPersonChildren
    template_name = 'demopersonchildren_list.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list = self.object_list)
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        res_format = request.GET.get('format')
        if res_format and res_format.lower() in 'json':
            return self.render_obj_to_json(context)
        if res_format and res_format.lower() in 'xml':
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemopersonchildrenCreateView(CreateView):
    model = DemoPersonChildren
    success_url = reverse_lazy('demopersonchildren_list')
    template_name = 'demopersonchildren_create.html'


class DemopersonchildrenDetailView(DetailView, AJAXResponseMixin):
    model = DemoPersonChildren
    template_name = 'demopersonchildren_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        res_format = request.GET.get('format')
        if res_format and 'json' in res_format.lower():
            return self.render_obj_to_json(context)
        if res_format and 'xml' in res_format.lower():
            return self.render_obj_to_xml(context)
        return self.render_to_response(context)


class DemopersonchildrenUpdateView(UpdateView):
    model = DemoPersonChildren
    success_url = reverse_lazy('demopersonchildren_list')
    template_name = 'demopersonchildren_update.html'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.success_url)


class DemopersonchildrenDeleteView(DeleteView):
    model = DemoPersonChildren
    success_url = reverse_lazy('demopersonchildren_list')
    template_name = 'demopersonchildren_confirm_delete.html'



