survey.onCurrentPageChanging.add((survey, options) => {
  if (
    options.newCurrentPage.name.startsWith("AUT_") ||
    (options.isGoingBackward &&
      survey.visiblePages[
        options.newCurrentPage.visibleIndex - 1
      ]?.name.startsWith("AUT_"))
  ) {
    survey.navigationBar.getActionById("sv-nav-prev").visible = false;
  }
});

survey.onCurrentPageChanging.add((survey, options) => {
  if (options.newCurrentPage.name == "AUT_sznurek") {
    survey.addNavigationItem({
      id: "complete-AUT",
      title: "Zakończ AUT",
      action: () => {
        survey.currentPageNo = survey.getPageByName("AUT_patyk").num;
        survey.navigationBar.getActionById("complete-AUT").visible = false;
      },
      visibleIndex: 21,
      css: "nav-button",
      innerCss: "sd-btn",
    });
  } else if (options.oldCurrentPage.name == "AUT_patyk") {
    survey.navigationBar.getActionById("complete-AUT").visible = false;
  }
});

survey.onCurrentPageChanged.add((survey, options) => {
  const isPrevVisible =
    survey.navigationBar.getActionById("sv-nav-prev").visible;
  if (
    !isPrevVisible &&
    !/^AUT_/.test(options.oldCurrentPage.name) &&
    !survey.visiblePages[
      options.newCurrentPage.visibleIndex - 1
    ]?.name.startsWith("AUT_")
  ) {
    survey.navigationBar.getActionById("sv-nav-prev").visible = true;
  }
});
