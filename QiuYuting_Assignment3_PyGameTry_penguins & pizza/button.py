import pygame.font

class Button():
    
    def __init__(self,pg_settings,screen,msg):
        '''初始化按钮属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (200, 236, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #按钮的rect对象
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.left = 20
        self.rect.top = 20
        
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        '''将 msg 渲染为图像，并使其在按钮上居中'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        '''绘制一个用颜色填充的按钮，再绘制文本'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
