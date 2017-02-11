function downloadMe() {
var pdf = new jsPDF();
pdf.addHTML(document.body,function() {
    pdf.save('thanh.pdf');
})}
