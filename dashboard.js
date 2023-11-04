/* this is the page selector or u can say the sidebar buttons */
function showContent(contentId) {
    // Hide all content divs
    const contentDivs = document.querySelectorAll('.content-of-page div');
    for (const div of contentDivs) {
        div.style.display = 'none';
    }

    // Show the selected content div
    const selectedContent = document.getElementById(contentId);
    if (selectedContent) {
        selectedContent.style.display = 'flex';
    }
}

/* for the community page */
function investi(){ window.location.href="https://www.investmentnews.com"; }
        function yahoo(){ window.location.href="https://finance.yahoo.com/"; }
        function tradev(){ window.location.href="https://www.tradingview.com/"; }
        function money(){ window.location.href="https://MoneyControl.com"; }
        function conomic(){ window.location.href="https://tradingeconomics.com/"; }
        function nse(){ window.location.href="https://www.nseindia.com/"; }