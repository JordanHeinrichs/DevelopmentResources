$('document').ready(function(){
    $('#updateButton').click(function() {
        $.post('',{}, function(data) {
            if (!data) {
                return;
            }
            $('#currentTime').text(data.time);
            $('#totalCpu').text(data.totalCpu);
            $("#cpuUsage").text(data.cpuUsage);
            $('#totalRam').text(data.totalRam);
            $('#usedRam').text(data.usedRam);
        });
    });
});
