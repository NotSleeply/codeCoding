const dog = {
  name: "旺财",
  sayName() {
    console.log(this.name);
  },
  eat(food) {
    console.log(`${this.name} 在吃${food}`);
  },
  eats(food1, food2) {
    console.log(`${this.name} 在吃${food1}和${food2}`);
  },
};

const cat = {
  name: "咪咪",
};

// call 会立即执行函数，并且改变 this 指向
dog.sayName.call(cat); // 输出 '咪咪'
dog.eat.call(cat, "🐟"); // 输出 '咪咪 在吃🐟'

dog.sayName.apply(cat); // 输出 '咪咪'

dog.eats.call(cat, "🐟", "🐔"); // 输出 '咪咪 在吃🐟和🐔'

dog.eats.apply(cat, ["🐟", "🐔"]); // 输出 '咪咪 在吃🐟和🐔'

const boundSayName = dog.eats.bind(cat);
boundSayName("🐟", "🐔"); // 输出 '咪咪 在吃🐟和🐔'