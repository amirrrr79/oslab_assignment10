import random
import arcade

class snake(arcade.Sprite) :  
    def __init__(self):
        super().__init__()  

        self.width=16
        self.height=16
        self.color=arcade.color.BLUE
        self.center_x=250
        self.center_y=250
        self.speed=1.7
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.body = []
        self.body.append([self.center_x,self.center_y])       

    def draw(self):
        for index, item in enumerate(self.body):
             arcade.draw_rectangle_filled(item[0], item[1],self.width,self.height,self.color)
             
    def move(self):

        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y
            

    def eat(self, food):

        if  food == 'apple':
            self.score += 1
            self.body.append([self.body[len(self.body)-1][0]+3000, self.body[len(self.body)-1][1]])
            self.body.append([self.body[len(self.body)-1][0]+3000, self.body[len(self.body)-1][1]])
            self.body.append([self.body[len(self.body)-1][0]+3000, self.body[len(self.body)-1][1]])
            self.body.append([self.body[len(self.body)-1][0]+3000, self.body[len(self.body)-1][1]])
        elif food == 'p':
            self.score -=1    
            
        
class Apple(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.image = 'Apple.png'  
        self.apple = arcade.Sprite(self.image, 0.02)    
        self.apple.center_x = random.randint(10, 480)  
        self.apple.center_y = random.randint(10, 480)     
    def draw(self):
        self.apple.draw()

class p(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.image = 'p.png'
        self.p = arcade.Sprite(self.image, 0.05)     
        self.p.center_x = random.randint(10, 480)  
        self.p.center_y = random.randint(10, 480)
    def draw(self):
        self.p.draw()

class game(arcade.Window) : 

    def __init__(self):
        super().__init__(width=500,height=500,title=' snake game')  
        arcade.set_background_color(arcade.color.GREEN)
        
        self.snake = snake()  
        self.apple = Apple()  
        self.p=p()
        
    def on_draw(self): 
        arcade.start_render()  
        self.snake.draw()
        self.apple.draw()
        self.p.draw()
        arcade.draw_text('score='+ str(self.snake.score),5,30,arcade.color.BLACK,15)
        if self.snake.score <0 or self.snake.center_x>=500 or self.snake.center_x<=0 or self.snake.center_y>=500 or self.snake.center_y<=0:
            arcade.draw_text('game over',120,250,arcade.color.RED,60)
            self.snake=snake()
        
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.apple.apple):
            self.snake.eat('apple')
            self.apple = Apple()
    
        if arcade.check_for_collision(self.snake,self.p.p):
            self.snake.eat('p')
            self.p = p()



    def on_key_release(self, key, modifiers):
        
        if key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
            

play_game=game()  
arcade.run()