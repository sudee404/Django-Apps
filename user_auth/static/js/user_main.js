$(document).ready(function () {
	var colors = ["#ff0000", "#00ff00", "#0000ff"];
	var currentColor = 0;
	setInterval(function () {
		$("body main").animate(
			{
				backgroundColor: colors[currentColor],
			},
			1000
		);
		currentColor = (currentColor + 1) % colors.length;
	}, 2000);
});
