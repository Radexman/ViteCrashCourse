// ============ 03 Object Literals And this Keyword ============== //

const rectangle = {
	name: 'Rectangle 1',
	width: 10,
	height: 10,
	area: () => {
		return width * height;
	},
};

const rectangle2 = {
	name: 'Rectangle 2',
	width: 30,
	height: 20,
	area: () => {
		return width * height;
	},
};

console.log(rectangle2.area());
