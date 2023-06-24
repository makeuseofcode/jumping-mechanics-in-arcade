import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_RADIUS = 20
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 20
GRAVITY = 0.5

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Jumping Mechanics")
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2
        self.player_dy = 0
        self.platform_x = SCREEN_WIDTH // 2
        self.platform_y = SCREEN_HEIGHT // 4

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, self.player_y, PLAYER_RADIUS, arcade.color.BLUE)
        arcade.draw_rectangle_filled(self.platform_x, self.platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT, arcade.color.GREEN)

    def on_update(self, delta_time):
        self.player_dy -= GRAVITY
        self.player_y += self.player_dy

        if self.player_y < PLAYER_RADIUS + self.platform_y + PLATFORM_HEIGHT / 2:
            self.player_y = PLAYER_RADIUS + self.platform_y + PLATFORM_HEIGHT / 2
            self.player_dy = 0

game = GameWindow()
arcade.run()
