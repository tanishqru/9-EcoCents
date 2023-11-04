function toggleVisibility(elementId) {
    var element = document.getElementById(elementId);
    if (element.style.visibility === "hidden") {
      element.style.visibility = "visible";
    } else {
      element.style.visibility = "hidden"; // Set it to "visible" to make it stay visible
    }
    console.log(element.style.visibility);
  }

