"use strict";

var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var socket = io.connect('http://' + document.domain + ':' + location.port);
var draw_data = null;

socket.on('connect', function () {
    socket.emit('my event', {
        data: 'User Connected'
    });
});

socket.on('update', function (data) {
    //console.log(data);
    draw_data = data;
    window.requestAnimationFrame(function() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath();
        ctx.arc(draw_data.pos.x, draw_data.pos.y, 5, 0, 2 * Math.PI, true);
        ctx.stroke();
    });
});
