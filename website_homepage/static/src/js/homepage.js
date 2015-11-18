$(document).ready(function() {
    $('#fullpage').fullpage({
        verticalCentered: false,
        anchors: ['firstPage', 'secondPage', '3rdPage'],
        sectionsColor: ['#C63D0F', '#1BBC9B', '#7E8F7C'],
        slidesNavigation: true,
        navigation: true,
        navigationPosition: 'right',
        navigationTooltips: ['First page', 'Second page', 'Third and last page'],
        afterRender: function(){
           //playing the video
           $('video').get(0).play();
        }
    });
});