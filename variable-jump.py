import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_RADIUS = 20
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 20
GRAVITY = 0.5
JUMP_POWER_INCREMENT = 0.2
MAX_JUMP_POWER = 100

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Jumping Mechanics")
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2
        self.player_dy = 0
        self.platform_x = SCREEN_WIDTH // 2
        self.platform_y = SCREEN_HEIGHT // 4
        self.jump_pressed = False  # Track if the jump button is pressed
        self.jump_power = 0  # Track the power of the jump

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.player_y == PLAYER_RADIUS + self.platform_y + PLATFORM_HEIGHT / 2:
            self.jump_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.jump_pressed = False

    def update_jump_power(self):
        # Increase the jump power while the jump button is held
        if self.jump_pressed:
            self.jump_power += JUMP_POWER_INCREMENT
            if self.jump_power > MAX_JUMP_POWER:
                self.jump_power = MAX_JUMP_POWER
        else:
            if self.jump_power > 0:
                self.jump_power -= 1

    def on_update(self, delta_time):
        self.player_dy -= GRAVITY

        # Apply jump power to player's vertical velocity
        if self.player_y == PLAYER_RADIUS + self.platform_y + PLATFORM_HEIGHT / 2 and self.jump_power > 0:
            self.player_dy = self.jump_power

        self.player_y += self.player_dy

        if self.player_y < PLAYER_RADIUS + self.platform_y + PLATFORM_HEIGHT / 2:
            self.player_y = PLAYER_RADIUS + self.platform_y + PLATFORM_HEIGHT / 2
            self.player_dy = 0

        self.update_jump_power()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, self.player_y, PLAYER_RADIUS, arcade.color.BLUE)
        arcade.draw_rectangle_filled(self.platform_x, self.platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT, arcade.color.GREEN)

game = GameWindow()
arcade.run()
