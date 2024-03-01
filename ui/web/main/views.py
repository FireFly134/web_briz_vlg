from typing import Type

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Model
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import (
    AddressListForm,
    DispatcherListForm,
    MechanicsListForm,
    RoutersForm,
    SimCardForm,
    UserLoginForms,
)
from .models import (
    AddressList,
    DispatcherList,
    MechanicsList,
    Routers,
    SimCard,
)


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "main/index.html")


def user_login(
    request: HttpRequest, next_page: str = "home"
) -> HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect:
    if request.method == "POST":
        form = UserLoginForms(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.POST.get("login_next", ""))
    else:
        form = UserLoginForms()
        next_page = (
            request.GET.get("next", "")
            if request.GET.get("next") is not None
            else "home"
        )
    return render(
        request,
        "main/login.html",
        context={"form": form, "next_page": next_page},
    )


def user_logout(
    request: HttpRequest,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    logout(request)
    return redirect("home")


class PatternShowList(ListView):
    context_object_name: str = "list"

    def get_queryset(self):
        return self.model.objects.all()


class PatternUpdate(
    UpdateView,
):
    pk_url_kwarg = "info_id"
    context_object_name = "info"


@login_required
def pattern_delete(
    request: HttpRequest,
    info_id: int,
    model: Type[Model],
    url_name: str,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    info = model.objects.get(pk=info_id)
    if request.user.is_superuser:
        info.delete()
        return redirect(url_name)
    raise PermissionDenied()


class PatternCreate(CreateView):
    def form_valid(self, form):
        report = form.save(commit=False)
        report.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("что-то не так!")
        # Добавьте здесь необходимые действия для обработки невалидной формы
        errors = form.errors.as_data()
        print(errors)
        # Теперь переменная errors содержит информацию о том,
        # почему форма невалидна.
        return self.render_to_response(
            self.get_context_data(form=form, errors=errors)
        )


##############################################################################
##############################################################################
##############################################################################


class ShowAddressList(PatternShowList):
    form_class = AddressListForm
    model = AddressList
    template_name = "main/address/list.html"


class ShowDispatcherList(PatternShowList):
    form_class = DispatcherList
    model = DispatcherList
    template_name = "main/dispatcher/list.html"


class ShowMechanicsList(PatternShowList):
    form_class = MechanicsListForm
    model = MechanicsList
    template_name = "main/mechanics/list.html"


class ShowRoutersList(PatternShowList):
    form_class = RoutersForm
    model = Routers
    template_name = "main/routers/list.html"


class ShowSimCardList(PatternShowList):
    form_class = SimCardForm
    model = SimCard
    template_name = "main/simcard/list.html"


##############################################################################
##############################################################################
##############################################################################


class AddressUpdate(PatternUpdate):
    form_class = AddressListForm
    model = AddressList
    template_name = "main/address/edit.html"
    success_url = reverse_lazy("address_list")


class DispatcherUpdate(PatternUpdate):
    form_class = DispatcherList
    model = DispatcherList
    template_name = "main/dispatcher_and_mechanics/list.html"
    success_url = reverse_lazy("dispatcher_list")


class MechanicsUpdate(PatternUpdate):
    form_class = MechanicsListForm
    model = MechanicsList
    template_name = "main/dispatcher_and_mechanics/list.html"
    success_url = reverse_lazy("mechanics_list")


class RoutersUpdate(PatternUpdate):
    form_class = RoutersForm
    model = Routers
    template_name = "main/routers/list.html"
    success_url = reverse_lazy("routers_list")


class SimCardUpdate(PatternUpdate):
    form_class = SimCardForm
    model = SimCard
    template_name = "main/simcard/list.html"
    success_url = reverse_lazy("simcard_list")


##############################################################################
##############################################################################
##############################################################################


class AddressCreate(PatternCreate):
    form_class = AddressListForm
    model = AddressList
    template_name = "main/address/create.html"
    success_url = reverse_lazy("new_address")


class DispatcherCreate(PatternCreate):
    form_class = DispatcherListForm
    model = DispatcherList
    template_name = "main/dispatcher/create.html"
    success_url = reverse_lazy("new_dispatcher")


class MechanicsCreate(PatternCreate):
    form_class = MechanicsListForm
    model = MechanicsList
    template_name = "main/mechanics/create.html"
    success_url = reverse_lazy("new_mechanics")


class RoutersCreate(PatternCreate):
    form_class = RoutersForm
    model = Routers
    template_name = "main/routers/create.html"
    success_url = reverse_lazy("new_routers")


class SimCardCreate(PatternCreate):
    form_class = SimCardForm
    model = SimCard
    template_name = "main/simcard/create.html"
    success_url = reverse_lazy("new_simcard")


##############################################################################
##############################################################################
##############################################################################


@login_required
def address_delete(
    request: HttpRequest,
    info_id: int,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    model = AddressList
    url_name = "address_list"
    return pattern_delete(request, info_id, model, url_name)


@login_required
def dispatcher_delete(
    request: HttpRequest,
    info_id: int,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    model = DispatcherList
    url_name = "dispatcher_list"
    return pattern_delete(request, info_id, model, url_name)


@login_required
def mechanics_delete(
    request: HttpRequest,
    info_id: int,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    model = MechanicsList
    url_name = "mechanics_list"
    return pattern_delete(request, info_id, model, url_name)


@login_required
def routers_delete(
    request: HttpRequest,
    info_id: int,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    model = Routers
    url_name = "routers_list"
    return pattern_delete(request, info_id, model, url_name)


@login_required
def simcard_delete(
    request: HttpRequest,
    info_id: int,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    model = SimCard
    url_name = "simcard_list"
    return pattern_delete(request, info_id, model, url_name)
