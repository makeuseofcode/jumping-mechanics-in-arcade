import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_RADIUS = 20
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 20
GRAVITY = 0.5
AIR_DASH_DISTANCE = 100
MAX_AIR_DASHES = 2

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Jumping Mechanics")
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2
        self.player_dx = 0
        self.player_dy = 0
        self.platform_x = SCREEN_WIDTH // 2
        self.platform_y = SCREEN_HEIGHT // 4
        self.on_ground = False  # Track if the player is on the ground
        self.air_dashes = 0  # Track the number of air dashes performed
        self.can_air_dash = True  # Track if the player can perform an air dash

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.on_ground:
            self.player_dy = 10  # Perform a regular jump
        elif key == arcade.key.UP and self.air_dashes < MAX_AIR_DASHES and self.can_air_dash:
            self.player_dx = AIR_DASH_DISTANCE  # Adjust the air dash distance and direction as desired
            self.air_dashes += 1
            self.can_air_dash = False

    def on_update(self, delta_time):
        self.player_dy -= GRAVITY
        self.player_y += self.player_dy

        if self.player_y <= PLAYER_RADIUS + self.platform_y + PLATFORM_HEIGHT / 2:
            self.player_y = PLAYER_RADIUS + self.platform_y + PLATFORM_HEIGHT / 2
            self.player_dy = 0
            self.on_ground = True
        else:
            self.on_ground = False

        self.player_x += self.player_dx

        if self.player_x < PLAYER_RADIUS:
            self.player_x = PLAYER_RADIUS
            self.player_dx = 0
        elif self.player_x > SCREEN_WIDTH - PLAYER_RADIUS:
            self.player_x = SCREEN_WIDTH - PLAYER_RADIUS
            self.player_dx = 0

        if self.on_ground:
            self.air_dashes = 0
            self.can_air_dash = True

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, self.player_y, PLAYER_RADIUS, arcade.color.BLUE)
        arcade.draw_rectangle_filled(self.platform_x, self.platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT, arcade.color.GREEN)

game = GameWindow()
arcade.run()
