function generateBarCode() {
    // label template
    var html = $('<page style="margin: 0;"><table style="width: 98%; margin: 0;" border=0><tr><td style="width: 82%; text-align: center;font-size: 8pt;"><img id="barcode" style="height: 60%;width: 100%;"/><BR/><span style="font-size: 8pt;">{{ product.model.model_short_name }} FMIP: {{ product.FMIP }}</span></td><td style="width: 18%; text-align: center;">No<BR/>Test</td></tr></table></page>');
    // insert barcode
    $("#barcode", $(html)).JsBarcode('{{ product.serial_id }}');
    // prepare for html to jpg
    var iframe=document.createElement('iframe');
    $('body').append($(iframe));
    var iframedoc=iframe.contentDocument||iframe.contentWindow.document;
    $('body',$(iframedoc)).html($(html).html());
    // html to jpg
    html2canvas(iframedoc.body).then(function(canvas) {
        var pageData = canvas.toDataURL('image/jpeg', 1.0);
        // create a PDF creator
        var pdf = new jsPDF({
            orientation: "l",
            unit: "mm",
            format: [50.8, 21.8]
        });
        // add jpg to PDF
        pdf.addImage(pageData, 'JPEG', 0, 0, 5.08 * 3.75, 2.18 * 3.75);
        // print PDF
        printJS({printable:pdf.output('bloburl'), type:'pdf', showModal:true});
    });
}