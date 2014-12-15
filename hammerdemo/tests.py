import unittest
from django.test import TestCase, Client
from django.test import RequestFactory
import doctest
from django.core.urlresolvers import reverse, reverse_lazy
from hammerdemo import models
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
from hammerdemo.views import (
    
    DemopersonsiblingsListView,
    DemopersonsiblingsDetailView,
    DemopersonsiblingsCreateView,
    DemopersonsiblingsUpdateView,
    DemopersonsiblingsDeleteView,
    
    DemopersonListView,
    DemopersonDetailView,
    DemopersonCreateView,
    DemopersonUpdateView,
    DemopersonDeleteView,
    
    DemopersonparentsListView,
    DemopersonparentsDetailView,
    DemopersonparentsCreateView,
    DemopersonparentsUpdateView,
    DemopersonparentsDeleteView,
    
    DemofamilypetsListView,
    DemofamilypetsDetailView,
    DemofamilypetsCreateView,
    DemofamilypetsUpdateView,
    DemofamilypetsDeleteView,
    
    DemofamilyListView,
    DemofamilyDetailView,
    DemofamilyCreateView,
    DemofamilyUpdateView,
    DemofamilyDeleteView,
    
    DemofamilymembersListView,
    DemofamilymembersDetailView,
    DemofamilymembersCreateView,
    DemofamilymembersUpdateView,
    DemofamilymembersDeleteView,
    
    DemopetListView,
    DemopetDetailView,
    DemopetCreateView,
    DemopetUpdateView,
    DemopetDeleteView,
    
    DemopersonchildrenListView,
    DemopersonchildrenDetailView,
    DemopersonchildrenCreateView,
    DemopersonchildrenUpdateView,
    DemopersonchildrenDeleteView,
    
)




class DemopersonsiblingsListViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonsiblings_list"))
        view = DemopersonsiblingsListView.as_view(template_name='demopersonsiblings_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demopersonsiblings_list") + "?format=json")
        json_response = view(json_request)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demopersonsiblings_list") + "?format=xml")
        xml_response = view(xml_request)
        self.assertEqual(xml_response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonsiblings_list"))
        view = DemopersonsiblingsListView.as_view(template_name='demopersonsiblings_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 405)


class DemopersonsiblingsDetailViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonsiblings_detail", kwargs={'pk':1}))
        view = DemopersonsiblingsDetailView.as_view(template_name='demopersonsiblings_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonsiblings_detail", kwargs={'pk':1}))
        view = DemopersonsiblingsDetailView.as_view(template_name='demopersonsiblings_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 405)


class DemopersonsiblingsCreateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonsiblings_create"))
        view = DemopersonsiblingsCreateView.as_view(template_name='demopersonsiblings_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonsiblings_create"))
        view = DemopersonsiblingsCreateView.as_view(template_name='demopersonsiblings_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)


class DemopersonsiblingsUpdateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonsiblings_update", kwargs={'pk':1}))
        view = DemopersonsiblingsUpdateView.as_view(template_name='demopersonsiblings_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demopersonsiblings_update", kwargs={'pk':1}) + "?format=json")
        json_response = view(request, pk=1)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demopersonsiblings_update", kwargs={'pk':1}) + "?format=xml")
        xml_response = view(xml_request, pk=1)
        self.assertEqual(xml_request.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonsiblings_update", kwargs={'pk':1}))
        view = DemopersonsiblingsUpdateView.as_view(template_name='demopersonsiblings_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)


class DemopersonsiblingsDeleteViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonsiblings_delete", kwargs={'pk':1}))
        view = DemopersonsiblingsDeleteView.as_view(template_name='demopersonsiblings_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonsiblings_delete", kwargs={'pk':1}))
        view = DemopersonsiblingsDeleteView.as_view(template_name='demopersonsiblings_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)



class DemopersonListViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demoperson_list"))
        view = DemopersonListView.as_view(template_name='demoperson_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demoperson_list") + "?format=json")
        json_response = view(json_request)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demoperson_list") + "?format=xml")
        xml_response = view(xml_request)
        self.assertEqual(xml_response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demoperson_list"))
        view = DemopersonListView.as_view(template_name='demoperson_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 405)


class DemopersonDetailViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demoperson_detail", kwargs={'pk':1}))
        view = DemopersonDetailView.as_view(template_name='demoperson_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demoperson_detail", kwargs={'pk':1}))
        view = DemopersonDetailView.as_view(template_name='demoperson_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 405)


class DemopersonCreateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demoperson_create"))
        view = DemopersonCreateView.as_view(template_name='demoperson_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demoperson_create"))
        view = DemopersonCreateView.as_view(template_name='demoperson_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)


class DemopersonUpdateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demoperson_update", kwargs={'pk':1}))
        view = DemopersonUpdateView.as_view(template_name='demoperson_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demoperson_update", kwargs={'pk':1}) + "?format=json")
        json_response = view(request, pk=1)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demoperson_update", kwargs={'pk':1}) + "?format=xml")
        xml_response = view(xml_request, pk=1)
        self.assertEqual(xml_request.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demoperson_update", kwargs={'pk':1}))
        view = DemopersonUpdateView.as_view(template_name='demoperson_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)


class DemopersonDeleteViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demoperson_delete", kwargs={'pk':1}))
        view = DemopersonDeleteView.as_view(template_name='demoperson_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demoperson_delete", kwargs={'pk':1}))
        view = DemopersonDeleteView.as_view(template_name='demoperson_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)



class DemopersonparentsListViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonparents_list"))
        view = DemopersonparentsListView.as_view(template_name='demopersonparents_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demopersonparents_list") + "?format=json")
        json_response = view(json_request)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demopersonparents_list") + "?format=xml")
        xml_response = view(xml_request)
        self.assertEqual(xml_response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonparents_list"))
        view = DemopersonparentsListView.as_view(template_name='demopersonparents_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 405)


class DemopersonparentsDetailViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonparents_detail", kwargs={'pk':1}))
        view = DemopersonparentsDetailView.as_view(template_name='demopersonparents_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonparents_detail", kwargs={'pk':1}))
        view = DemopersonparentsDetailView.as_view(template_name='demopersonparents_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 405)


class DemopersonparentsCreateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonparents_create"))
        view = DemopersonparentsCreateView.as_view(template_name='demopersonparents_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonparents_create"))
        view = DemopersonparentsCreateView.as_view(template_name='demopersonparents_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)


class DemopersonparentsUpdateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonparents_update", kwargs={'pk':1}))
        view = DemopersonparentsUpdateView.as_view(template_name='demopersonparents_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demopersonparents_update", kwargs={'pk':1}) + "?format=json")
        json_response = view(request, pk=1)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demopersonparents_update", kwargs={'pk':1}) + "?format=xml")
        xml_response = view(xml_request, pk=1)
        self.assertEqual(xml_request.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonparents_update", kwargs={'pk':1}))
        view = DemopersonparentsUpdateView.as_view(template_name='demopersonparents_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)


class DemopersonparentsDeleteViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonparents_delete", kwargs={'pk':1}))
        view = DemopersonparentsDeleteView.as_view(template_name='demopersonparents_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonparents_delete", kwargs={'pk':1}))
        view = DemopersonparentsDeleteView.as_view(template_name='demopersonparents_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)



class DemofamilypetsListViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamilypets_list"))
        view = DemofamilypetsListView.as_view(template_name='demofamilypets_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demofamilypets_list") + "?format=json")
        json_response = view(json_request)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demofamilypets_list") + "?format=xml")
        xml_response = view(xml_request)
        self.assertEqual(xml_response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamilypets_list"))
        view = DemofamilypetsListView.as_view(template_name='demofamilypets_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 405)


class DemofamilypetsDetailViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamilypets_detail", kwargs={'pk':1}))
        view = DemofamilypetsDetailView.as_view(template_name='demofamilypets_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamilypets_detail", kwargs={'pk':1}))
        view = DemofamilypetsDetailView.as_view(template_name='demofamilypets_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 405)


class DemofamilypetsCreateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamilypets_create"))
        view = DemofamilypetsCreateView.as_view(template_name='demofamilypets_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamilypets_create"))
        view = DemofamilypetsCreateView.as_view(template_name='demofamilypets_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)


class DemofamilypetsUpdateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamilypets_update", kwargs={'pk':1}))
        view = DemofamilypetsUpdateView.as_view(template_name='demofamilypets_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demofamilypets_update", kwargs={'pk':1}) + "?format=json")
        json_response = view(request, pk=1)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demofamilypets_update", kwargs={'pk':1}) + "?format=xml")
        xml_response = view(xml_request, pk=1)
        self.assertEqual(xml_request.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamilypets_update", kwargs={'pk':1}))
        view = DemofamilypetsUpdateView.as_view(template_name='demofamilypets_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)


class DemofamilypetsDeleteViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamilypets_delete", kwargs={'pk':1}))
        view = DemofamilypetsDeleteView.as_view(template_name='demofamilypets_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamilypets_delete", kwargs={'pk':1}))
        view = DemofamilypetsDeleteView.as_view(template_name='demofamilypets_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)



class DemofamilyListViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamily_list"))
        view = DemofamilyListView.as_view(template_name='demofamily_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demofamily_list") + "?format=json")
        json_response = view(json_request)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demofamily_list") + "?format=xml")
        xml_response = view(xml_request)
        self.assertEqual(xml_response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamily_list"))
        view = DemofamilyListView.as_view(template_name='demofamily_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 405)


class DemofamilyDetailViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamily_detail", kwargs={'pk':1}))
        view = DemofamilyDetailView.as_view(template_name='demofamily_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamily_detail", kwargs={'pk':1}))
        view = DemofamilyDetailView.as_view(template_name='demofamily_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 405)


class DemofamilyCreateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamily_create"))
        view = DemofamilyCreateView.as_view(template_name='demofamily_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamily_create"))
        view = DemofamilyCreateView.as_view(template_name='demofamily_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)


class DemofamilyUpdateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamily_update", kwargs={'pk':1}))
        view = DemofamilyUpdateView.as_view(template_name='demofamily_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demofamily_update", kwargs={'pk':1}) + "?format=json")
        json_response = view(request, pk=1)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demofamily_update", kwargs={'pk':1}) + "?format=xml")
        xml_response = view(xml_request, pk=1)
        self.assertEqual(xml_request.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamily_update", kwargs={'pk':1}))
        view = DemofamilyUpdateView.as_view(template_name='demofamily_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)


class DemofamilyDeleteViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamily_delete", kwargs={'pk':1}))
        view = DemofamilyDeleteView.as_view(template_name='demofamily_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamily_delete", kwargs={'pk':1}))
        view = DemofamilyDeleteView.as_view(template_name='demofamily_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)



class DemofamilymembersListViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamilymembers_list"))
        view = DemofamilymembersListView.as_view(template_name='demofamilymembers_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demofamilymembers_list") + "?format=json")
        json_response = view(json_request)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demofamilymembers_list") + "?format=xml")
        xml_response = view(xml_request)
        self.assertEqual(xml_response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamilymembers_list"))
        view = DemofamilymembersListView.as_view(template_name='demofamilymembers_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 405)


class DemofamilymembersDetailViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamilymembers_detail", kwargs={'pk':1}))
        view = DemofamilymembersDetailView.as_view(template_name='demofamilymembers_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamilymembers_detail", kwargs={'pk':1}))
        view = DemofamilymembersDetailView.as_view(template_name='demofamilymembers_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 405)


class DemofamilymembersCreateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamilymembers_create"))
        view = DemofamilymembersCreateView.as_view(template_name='demofamilymembers_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamilymembers_create"))
        view = DemofamilymembersCreateView.as_view(template_name='demofamilymembers_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)


class DemofamilymembersUpdateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamilymembers_update", kwargs={'pk':1}))
        view = DemofamilymembersUpdateView.as_view(template_name='demofamilymembers_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demofamilymembers_update", kwargs={'pk':1}) + "?format=json")
        json_response = view(request, pk=1)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demofamilymembers_update", kwargs={'pk':1}) + "?format=xml")
        xml_response = view(xml_request, pk=1)
        self.assertEqual(xml_request.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamilymembers_update", kwargs={'pk':1}))
        view = DemofamilymembersUpdateView.as_view(template_name='demofamilymembers_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)


class DemofamilymembersDeleteViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demofamilymembers_delete", kwargs={'pk':1}))
        view = DemofamilymembersDeleteView.as_view(template_name='demofamilymembers_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demofamilymembers_delete", kwargs={'pk':1}))
        view = DemofamilymembersDeleteView.as_view(template_name='demofamilymembers_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)



class DemopetListViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopet_list"))
        view = DemopetListView.as_view(template_name='demopet_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demopet_list") + "?format=json")
        json_response = view(json_request)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demopet_list") + "?format=xml")
        xml_response = view(xml_request)
        self.assertEqual(xml_response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopet_list"))
        view = DemopetListView.as_view(template_name='demopet_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 405)


class DemopetDetailViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopet_detail", kwargs={'pk':1}))
        view = DemopetDetailView.as_view(template_name='demopet_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopet_detail", kwargs={'pk':1}))
        view = DemopetDetailView.as_view(template_name='demopet_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 405)


class DemopetCreateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopet_create"))
        view = DemopetCreateView.as_view(template_name='demopet_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopet_create"))
        view = DemopetCreateView.as_view(template_name='demopet_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)


class DemopetUpdateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopet_update", kwargs={'pk':1}))
        view = DemopetUpdateView.as_view(template_name='demopet_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demopet_update", kwargs={'pk':1}) + "?format=json")
        json_response = view(request, pk=1)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demopet_update", kwargs={'pk':1}) + "?format=xml")
        xml_response = view(xml_request, pk=1)
        self.assertEqual(xml_request.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopet_update", kwargs={'pk':1}))
        view = DemopetUpdateView.as_view(template_name='demopet_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)


class DemopetDeleteViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopet_delete", kwargs={'pk':1}))
        view = DemopetDeleteView.as_view(template_name='demopet_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopet_delete", kwargs={'pk':1}))
        view = DemopetDeleteView.as_view(template_name='demopet_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)



class DemopersonchildrenListViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonchildren_list"))
        view = DemopersonchildrenListView.as_view(template_name='demopersonchildren_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demopersonchildren_list") + "?format=json")
        json_response = view(json_request)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demopersonchildren_list") + "?format=xml")
        xml_response = view(xml_request)
        self.assertEqual(xml_response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonchildren_list"))
        view = DemopersonchildrenListView.as_view(template_name='demopersonchildren_list.html')
        response = view(request)
        self.assertEqual(response.status_code, 405)


class DemopersonchildrenDetailViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonchildren_detail", kwargs={'pk':1}))
        view = DemopersonchildrenDetailView.as_view(template_name='demopersonchildren_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonchildren_detail", kwargs={'pk':1}))
        view = DemopersonchildrenDetailView.as_view(template_name='demopersonchildren_detail.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 405)


class DemopersonchildrenCreateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonchildren_create"))
        view = DemopersonchildrenCreateView.as_view(template_name='demopersonchildren_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonchildren_create"))
        view = DemopersonchildrenCreateView.as_view(template_name='demopersonchildren_create.html')
        response = view(request)
        self.assertEqual(response.status_code, 200)


class DemopersonchildrenUpdateViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonchildren_update", kwargs={'pk':1}))
        view = DemopersonchildrenUpdateView.as_view(template_name='demopersonchildren_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)
        json_request = RequestFactory().get(reverse_lazy("demopersonchildren_update", kwargs={'pk':1}) + "?format=json")
        json_response = view(request, pk=1)
        self.assertEqual(json_response.status_code, 200)
        xml_request = RequestFactory().get(reverse_lazy("demopersonchildren_update", kwargs={'pk':1}) + "?format=xml")
        xml_response = view(xml_request, pk=1)
        self.assertEqual(xml_request.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonchildren_update", kwargs={'pk':1}))
        view = DemopersonchildrenUpdateView.as_view(template_name='demopersonchildren_update.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)


class DemopersonchildrenDeleteViewTest(TestCase):
    multi_db = True
    def setUp(self):
        self.client = Client()

    def test_get(self):
        request = RequestFactory().get(reverse_lazy("demopersonchildren_delete", kwargs={'pk':1}))
        view = DemopersonchildrenDeleteView.as_view(template_name='demopersonchildren_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        request = RequestFactory().post(reverse_lazy("demopersonchildren_delete", kwargs={'pk':1}))
        view = DemopersonchildrenDeleteView.as_view(template_name='demopersonchildren_delete.html')
        response = view(request, pk=1)
        self.assertEqual(response.status_code, 200)




class DemoPersonSiblingsTest(TestCase):
    multi_db = True
    def setUp(self):
        self.object = DemoPersonSiblings.objects.create(id = 1, from_person_id = 1, to_person_id = 1)

    def test_unicode(self):
        self.assertEqual(self.object.__unicode__() == str(self.object.pk))

    def tearDown(self):
        self.object.delete()

class DemoPersonTest(TestCase):
    multi_db = True
    def setUp(self):
        self.object = DemoPerson.objects.create(id = 1, sex = 1, first = 'test', last = 'test', age = 1, alive = True, spouse_id = 1)

    def test_unicode(self):
        self.assertEqual(self.object.__unicode__() == str(self.object.pk))

    def tearDown(self):
        self.object.delete()

class DemoPersonParentsTest(TestCase):
    multi_db = True
    def setUp(self):
        self.object = DemoPersonParents.objects.create(id = 1, from_person_id = 1, to_person_id = 1)

    def test_unicode(self):
        self.assertEqual(self.object.__unicode__() == str(self.object.pk))

    def tearDown(self):
        self.object.delete()

class DemoFamilyPetsTest(TestCase):
    multi_db = True
    def setUp(self):
        self.object = DemoFamilyPets.objects.create(id = 1, family_id = 1, pet_id = 1)

    def test_unicode(self):
        self.assertEqual(self.object.__unicode__() == str(self.object.pk))

    def tearDown(self):
        self.object.delete()

class DemoFamilyTest(TestCase):
    multi_db = True
    def setUp(self):
        self.object = DemoFamily.objects.create(id = 1, name = 'test')

    def test_unicode(self):
        self.assertEqual(self.object.__unicode__() == str(self.object.pk))

    def tearDown(self):
        self.object.delete()

class DemoFamilyMembersTest(TestCase):
    multi_db = True
    def setUp(self):
        self.object = DemoFamilyMembers.objects.create(id = 1, family_id = 1, person_id = 1)

    def test_unicode(self):
        self.assertEqual(self.object.__unicode__() == str(self.object.pk))

    def tearDown(self):
        self.object.delete()

class DemoPetTest(TestCase):
    multi_db = True
    def setUp(self):
        self.object = DemoPet.objects.create(id = 1, sex = 1, owner_id = 1, name = 'test', age = 1, species = 'test', alive = True)

    def test_unicode(self):
        self.assertEqual(self.object.__unicode__() == str(self.object.pk))

    def tearDown(self):
        self.object.delete()

class DemoPersonChildrenTest(TestCase):
    multi_db = True
    def setUp(self):
        self.object = DemoPersonChildren.objects.create(id = 1, from_person_id = 1, to_person_id = 1)

    def test_unicode(self):
        self.assertEqual(self.object.__unicode__() == str(self.object.pk))

    def tearDown(self):
        self.object.delete()



# to enable doctests
#def load_tests(loader, tests, ignore):
#    tests.addTests(doctest.DocTestSuite(models))
#    return tests
