import View from "../View/index.js";

function view(url) {

    const view = new View({
        url: url,
        urlChange: true,
        callback: function () {

            // Si ce n'est pas une vue partielle, alors on initialise la page
            if ('!/^\/_partials\//.test(url)') {
                initializesPage();
            }

        }
    });

    view.display();

}

export default view;