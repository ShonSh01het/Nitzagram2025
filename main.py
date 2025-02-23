import pygame
from helpers import screen
from constants import *
from helpers import from_text_to_array, center_text, mouse_in_button
from buttons import like_button, comment_button, view_more_comments_button, click_post_button


class Post:
    """
    A class used to represent post on Nitzagram
    """

    def __init__(self, user_name, location, likes_counter, comments, description):
        self.user_name = user_name
        self.location = location
        self.likes_counter = likes_counter
        self.comments = comments
        self.description = description

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        myfont = pygame.font.Font('fonts/Roboto_Condensed-Black.ttf', 15)
        write_user = myfont.render(str(self.user_name), True, BLACK)
        screen.blit(write_user, (USER_NAME_X_POS, USER_NAME_Y_POS))
        write_location = myfont.render(str(self.location), True, LIGHT_GRAY)
        screen.blit(write_location, (USER_NAME_X_POS, USER_NAME_Y_POS + 15))
        write_likes_counter = myfont.render("Liked by " + str(self.likes_counter) + " users", True, GREY)
        screen.blit(write_likes_counter, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))
        write_description = myfont.render(str(self.description), True, BLACK)
        screen.blit(write_description, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))
        COMMENT_X_POS = FIRST_COMMENT_X_POS
        COMMENT_Y_POS = FIRST_COMMENT_Y_POS
        if len(self.comments) >= NUM_OF_COMMENTS_TO_DISPLAY:
            for comment in range(NUM_OF_COMMENTS_TO_DISPLAY):
                write_comment = myfont.render(str(self.comments[comment]), True, GREY)
                screen.blit(write_comment, (COMMENT_X_POS, COMMENT_Y_POS))
                COMMENT_Y_POS += 15
        else:
            for comment in range(len(self.comments)):
                write_comment = myfont.render(str(self.comments[comment]), True, GREY)
                screen.blit(write_comment, (COMMENT_X_POS, COMMENT_Y_POS))
                COMMENT_Y_POS += 15

    def add_like(self):
        self.likes_counter = self.likes_counter + 1
        return



    def add_comment(self):
        return


class Image_Post(Post):
    def __init__(self, image, user_name, location, likes_counter, comments, description):
        super().__init__(user_name, location, likes_counter, comments, description)
        self.image = image

    def display(self):
        super().display()
        post_image = pygame.image.load(self.image)
        small_image = pygame.transform.smoothscale(post_image, (POST_WIDTH, POST_HEIGHT))
        screen.blit(small_image, (POST_X_POS, POST_Y_POS))


class Text_Post(Post):
    def __init__(self, text, color, backgraund_color, user_name, location, likes_counter, comments, description):
        super().__init__(user_name, location, likes_counter, comments, description)
        self.text = text
        self.color = color
        self.backgraund_color = backgraund_color

    def display(self):
        super().display()
        backgraund = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        backgraund.fill(self.backgraund_color)
        screen.blit(backgraund, (POST_X_POS, POST_Y_POS))
        myfont = pygame.font.Font('fonts/Roboto_Condensed-Black.ttf', TEXT_POST_FONT_SIZE)
        for i in range(len(from_text_to_array(self.text))):
            write_post = myfont.render(from_text_to_array(self.text)[i], True, self.color, self.backgraund_color)
            screen.blit(write_post, center_text(len(self.text) / LINE_MAX_LENGTH, write_post, i))


def main():
    # Set up the game display, clock and headline
    pygame.init()
    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    heart_image = pygame.image.load('Images/like.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    heart_image = pygame.transform.scale(heart_image, (LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT))

    test = Text_Post('Hello every one', 'Red', 'Green', 'gleb', 'israel', 5, ["it is true", "Really"],
                     'i hate this project')
    like_status = False
    running = True
    while running:

        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_in_button(like_button, pygame.mouse.get_pos()):
                    test.add_like()
                    if not like_status:
                        like_status = True

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        test.display()
        pygame.draw.rect(screen,(255,255,255), (26, 551, 308, 38))
        if like_status:
            heart_rect = heart_image.get_rect(
                center=(LIKE_BUTTON_X_POS + 0.067 * WINDOW_WIDTH / 2 + 0.45, LIKE_BUTTON_Y_POS + 0.033 * WINDOW_HEIGHT /2 - 1))

            # Draw the heart image on the screen
            screen.blit(heart_image, heart_rect)
        #    pygame.display.flip()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
