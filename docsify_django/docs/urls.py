from django.urls import path

from docsify_django.docs.views import (
    DocsifyView,
    docsify_index,
    docsify_sidebar,
    # section 1
    docsify_section1_part1,
    docsify_section1_part2,
    docsify_section1_part3,
    # section 2
    docsify_section2_part1,
    docsify_section2_part2,
    docsify_section2_part3,
    # section 3
    docsify_section3_part1,
    docsify_section3_part2,
    docsify_section3_part3,
    # section 4
    docsify_section4_part1,
    docsify_section4_part2,
    docsify_section4_part3,
    # section 5
    docsify_section5_part1,
    docsify_section5_part2,
    docsify_section5_part3,
)

app_name = "docs"

urlpatterns = [
    path("", DocsifyView.as_view(), name="docsify-view"),
    path("index.md", docsify_index, name="docsify-index"),
    path("_sidebar.md", docsify_sidebar, name="docsify-sidebar"),
    # section 1
    path("section-01/index.md", docsify_section1_part1, name="docsify-sec1-part1"),
    path("section-01/section.md", docsify_section1_part2, name="docsify-sec1-part2"),
    path(
        "section-01/another-section.md",
        docsify_section1_part3,
        name="docsify-sec1-part3",
    ),
    # section 2
    path("section-02/index.md", docsify_section2_part1, name="docsify-sec2-part1"),
    path("section-02/stuff.md", docsify_section2_part2, name="docsify-sec2-part2"),
    path(
        "section-02/more-stuff.md",
        docsify_section2_part3,
        name="docsify-sec2-part3",
    ),
    # section 3
    path("section-03/index.md", docsify_section3_part1, name="docsify-sec3-part1"),
    path(
        "section-03/lorem-ipsum.md", docsify_section3_part2, name="docsify-sec3-part2"
    ),
    path(
        "section-03/lorem-docsum.md",
        docsify_section3_part3,
        name="docsify-sec3-part3",
    ),
    # section 4
    path("section-04/index.md", docsify_section4_part1, name="docsify-sec4-part1"),
    path(
        "section-04/look-some-docs.md",
        docsify_section4_part2,
        name="docsify-sec4-part2",
    ),
    path(
        "section-04/something-here.md",
        docsify_section4_part3,
        name="docsify-sec4-part3",
    ),
    # section 5
    path("section-05/index.md", docsify_section5_part1, name="docsify-sec5-part1"),
    path("section-05/something.md", docsify_section5_part2, name="docsify-sec5-part2"),
    path(
        "section-05/another-thing.md",
        docsify_section5_part3,
        name="docsify-sec5-part3",
    ),
]
