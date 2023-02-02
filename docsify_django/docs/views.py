from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DocsifyView(LoginRequiredMixin, TemplateView):
    """
    Documentation, powered by <https://docsify.js.org>
    """

    login_url = "/login/"
    redirect_field_name = "next"
    template_name = "docs/index.html"


# The rest of the views below are for each markdown file.
# See https://stackoverflow.com/a/58901221


@login_required
def docsify_index(request):
    """index.md in docs root"""
    context = {}
    return render(request, "docs/index.md", context)


@login_required
def docsify_sidebar(request):
    """_sidebar.md in docs root"""
    context = {}
    return render(request, "docs/_sidebar.md", context)


@login_required
def docsify_section1_part1(request):
    """index.md in section-01/"""
    context = {}
    return render(request, "docs/section-01/index.md", context)


@login_required
def docsify_section1_part2(request):
    """section.md in section-01/"""
    context = {}
    return render(request, "docs/section-01/section.md", context)


@login_required
def docsify_section1_part3(request):
    """another-section.md in section-01/"""
    context = {}
    return render(request, "docs/section-01/another-section.md", context)


@login_required
def docsify_section2_part1(request):
    """index.md in section-02/"""
    context = {}
    return render(request, "docs/section-02/index.md", context)


@login_required
def docsify_section2_part2(request):
    """stuff.md in section-02/"""
    context = {}
    return render(request, "docs/section-02/stuff.md", context)


@login_required
def docsify_section2_part3(request):
    """more-stuff.md in section-02/"""
    context = {}
    return render(request, "docs/section-02/more-stuff.md", context)


@login_required
def docsify_section3_part1(request):
    """index.md in section-03/"""
    context = {}
    return render(request, "docs/section-03/index.md", context)


@login_required
def docsify_section3_part2(request):
    """lorem-ipsum.md in section-03/"""
    context = {}
    return render(request, "docs/section-03/lorem-ipsum.md", context)


@login_required
def docsify_section3_part3(request):
    """lorem-docsum.md in section-03/"""
    context = {}
    return render(request, "docs/section-03/lorem-docsum.md", context)


@login_required
def docsify_section4_part1(request):
    """index.md in section-04/"""
    context = {}
    return render(request, "docs/section-04/index.md", context)


@login_required
def docsify_section4_part2(request):
    """look-some-docs.md in section-04/"""
    context = {}
    return render(request, "docs/section-04/look-some-docs.md", context)


@login_required
def docsify_section4_part3(request):
    """something-here.md in section-04/"""
    context = {}
    return render(request, "docs/section-04/something-here.md", context)


@login_required
def docsify_section5_part1(request):
    """index.md in section-05/"""
    context = {}
    return render(request, "docs/section-05/index.md", context)


@login_required
def docsify_section5_part2(request):
    """something.md in section-05/"""
    context = {}
    return render(request, "docs/section-05/something.md", context)


@login_required
def docsify_section5_part3(request):
    """another-thing.md in section-05/"""
    context = {}
    return render(request, "docs/section-05/another-thing.md", context)
