from manim import (
    PI,
    DOWN,
    GREY_A,
    LEFT,
    RED,
    BLUE,
    RIGHT,
    UL,
    UP,
    WHITE,
    Arrow,
    CurvedArrow,
    SurroundingRectangle,
    Circle,
    Circumscribe,
    Create,
    Cross,
    DoubleArrow,
    FadeIn,
    FadeOut,
    Group,
    GrowArrow,
    GrowFromCenter,
    ImageMobject,
    Rectangle,
    RoundedRectangle,
    Scene,
    ShowPassingFlash,
    SVGMobject,
    Text,
    TypeWithCursor,
    Table,
)
from manim_slides.slide import Slide

CURSOR = Rectangle(
    color=GREY_A,
    fill_color=GREY_A,
    fill_opacity=1.0,
    height=1,
    width=0.2,
)


class ThreeLayerAppScene(Slide):
    def construct(self):
        # Initial scene with 3-layer application explain
        three_layer_app_group = Group()
        angular_icon = SVGMobject(file_name="../assets/angular-logo.svg")
        angular_icon.add(
            Text(text="Angular Front-end").scale(0.5).next_to(angular_icon, DOWN)
        )
        self.play(GrowFromCenter(angular_icon))
        three_layer_app_group.add(angular_icon)
        self.next_slide()

        first_arrow = DoubleArrow(tip_length=0.2, buff=0)
        self.add(first_arrow)
        self.play(
            GrowFromCenter(first_arrow.center()),
            angular_icon.animate.next_to(first_arrow, LEFT),
        )
        three_layer_app_group.add(first_arrow)

        python_icon = ImageMobject(filename_or_array="../assets/python-logo.png")
        python_icon.scale(0.5)
        python_icon.add(Text(text="REST API").scale(0.5).next_to(python_icon, DOWN))
        self.play(
            GrowFromCenter(python_icon),
            three_layer_app_group.animate.next_to(python_icon, LEFT),
        )
        three_layer_app_group.add(python_icon)
        self.next_slide()

        second_arrow = DoubleArrow(tip_length=0.2, buff=0)
        self.add(second_arrow)
        second_arrow.next_to(three_layer_app_group, RIGHT)
        self.play(
            GrowFromCenter(second_arrow),
        )
        three_layer_app_group.add(second_arrow)

        postgresql_icon = SVGMobject(file_name="../assets/postgresql-logo.svg")
        postgresql_icon.add(
            Text(text="SQL Database").scale(0.5).next_to(postgresql_icon, DOWN)
        )
        self.add(postgresql_icon)
        postgresql_icon.next_to(three_layer_app_group, RIGHT)
        self.play(GrowFromCenter(postgresql_icon))
        three_layer_app_group.add(postgresql_icon)
        self.next_slide()

        question_text = Text(text="How do we deploy this?")
        question_text.scale(0.8).next_to(three_layer_app_group, UP, buff=1)
        cursor = (
            CURSOR.copy().scale(0.8).move_to(question_text[0])
        )  # Position the cursor
        self.add(question_text)
        self.play(TypeWithCursor(text=question_text, cursor=cursor, time_per_char=0.05))
        self.next_slide()


class EvolutionOfDeploymentSlide(Slide):
    def construct(self):
        header_text = Text(text="The Evolution Of Software Deployment")
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()

        icons_group = Group()

        server_icon = SVGMobject(file_name="../assets/server-icon.svg")
        server_text = Text(text="Bare-Metal").scale(0.5)
        server_icon.add(server_text.next_to(server_icon, DOWN, buff=0.5))

        vm_icon = SVGMobject(
            file_name="../assets/virtual-machine-icon.svg",
        )
        vm_text = Text(text="Virtual Machines").scale(0.5)
        vm_icon.add(vm_text.next_to(vm_icon, DOWN, buff=0.5))
        vm_icon.scale_to_fit_height(server_icon.height)
        vm_icon.next_to(server_icon, RIGHT, buff=2)

        docker_icon = SVGMobject(
            file_name="../assets/container-icon.svg",
        )
        docker_text = Text(text="Containers").scale(0.5)
        docker_icon.add(docker_text.next_to(docker_icon, DOWN, buff=0.5))
        docker_icon.scale_to_fit_height(server_icon.height)
        docker_icon.next_to(vm_icon, RIGHT, buff=2)

        icons_group.add(server_icon, vm_icon, docker_icon)
        icons_group.center()

        self.play(FadeIn(server_icon))

        self.next_slide()
        self.play(FadeIn(vm_icon))

        self.next_slide()
        self.play(FadeIn(docker_icon))


class BareMetalDeployment(Slide):
    def construct(self):
        header_text = Text(text="Bare-Metal Deployment")
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()
        server_border = RoundedRectangle(
            width=13, height=6, stroke_width=1, corner_radius=0.1
        )
        server_border.next_to(header_text, DOWN, buff=0.5)

        server_icon = SVGMobject(file_name="../assets/server-icon.svg").scale(0.7)
        server_icon.move_to(server_border.get_corner(UP + RIGHT))

        dependencies_header = Text(text="Dependencies").scale(0.5)
        dependencies_border = RoundedRectangle(
            width=5, height=5, stroke_width=0.7, corner_radius=0.1
        )
        dependencies_border.align_to(server_border, direction=UP + LEFT)
        dependencies_border.shift(LEFT * -0.5, UP * -0.5)
        dependencies_header.next_to(dependencies_border.get_top(), DOWN, buff=0.2)

        application_header = Text(text="Application").scale(0.5)
        application_border = RoundedRectangle(
            width=5, height=5, stroke_width=0.7, corner_radius=0.1
        )
        application_border.align_to(server_border, direction=UP + RIGHT)
        application_border.shift(RIGHT * -0.7, UP * -0.5)
        application_header.next_to(application_border.get_top(), DOWN, buff=0.2)

        python_icon = ImageMobject(filename_or_array="../assets/python-logo.png")
        nginx_icon = SVGMobject(file_name="../assets/nginx-logo.svg")
        iis_icon = SVGMobject(file_name="../assets/iis-logo.svg")

        python_icon.scale(0.4).align_to(dependencies_border, direction=UP + LEFT)
        python_icon.shift(DOWN * 1).shift(RIGHT * 0.5)

        nginx_icon.scale(0.7).align_to(dependencies_border, direction=UP + RIGHT)
        nginx_icon.shift(DOWN * 1.5).shift(LEFT * 0.5)

        iis_icon.add_background_rectangle(color=WHITE, opacity=1, buff=0.5)
        iis_icon.scale(0.5).align_to(dependencies_border, direction=DOWN + LEFT)
        iis_icon.shift(UP * 0.2).shift(RIGHT * 0.5)

        application_code = SVGMobject(file_name="../assets/code-icon.svg")
        application_code.move_to(application_border.get_center())

        self.play(Create(server_border), GrowFromCenter(server_icon))

        self.next_slide()
        self.play(Create(dependencies_border), FadeIn(dependencies_header))

        self.next_slide()
        self.play(
            GrowFromCenter(python_icon),
            GrowFromCenter(nginx_icon),
            GrowFromCenter(iis_icon),
        )

        self.next_slide()
        self.play(Create(application_border), FadeIn(application_header))

        self.next_slide()
        self.play(GrowFromCenter(application_code))


class VirtualMachineDeployment(Slide):
    def construct(self):
        header_text = Text(text="Virtual Machines")
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()
        server_border = RoundedRectangle(
            width=13, height=6, stroke_width=1, corner_radius=0.1
        )
        server_border.next_to(header_text, DOWN, buff=0.5)

        server_icon = SVGMobject(file_name="../assets/server-icon.svg").scale(0.7)
        server_icon.move_to(server_border.get_corner(UP + RIGHT))

        self.play(Create(server_border), GrowFromCenter(server_icon))
        self.next_slide()

        virtual_machine_icon_1 = SVGMobject(
            file_name="../assets/virtual-machine-icon.svg"
        ).scale(0.3)
        virtual_machine_border_1 = RoundedRectangle(
            width=5, height=5, stroke_width=0.7, corner_radius=0.1
        )
        virtual_machine_border_1.align_to(server_border, direction=UP + LEFT)
        virtual_machine_border_1.shift(LEFT * -0.5, UP * -0.5)
        virtual_machine_icon_1.move_to(virtual_machine_border_1.get_corner(UP + RIGHT))

        self.play(
            Create(virtual_machine_border_1), GrowFromCenter(virtual_machine_icon_1)
        )

        virtual_machine_icon_2 = SVGMobject(
            file_name="../assets/virtual-machine-icon.svg"
        ).scale(0.3)
        virtual_machine_border_2 = RoundedRectangle(
            width=5, height=5, stroke_width=0.7, corner_radius=0.1
        )
        virtual_machine_border_2.align_to(server_border, direction=UP + RIGHT)
        virtual_machine_border_2.shift(RIGHT * -1, UP * -0.5)
        virtual_machine_icon_2.move_to(virtual_machine_border_2.get_corner(UP + RIGHT))

        self.play(
            Create(virtual_machine_border_2), GrowFromCenter(virtual_machine_icon_2)
        )

        self.next_slide()

        app1_header = Text(text="App1").scale(0.5)
        app1_header.next_to(virtual_machine_border_1.get_top(), DOWN, buff=0.2)

        app2_header = Text(text="App2").scale(0.5)
        app2_header.next_to(virtual_machine_border_2.get_top(), DOWN, buff=0.2)

        self.play(FadeIn(app1_header), FadeIn(app2_header))

        self.next_slide()

        python_icon_1 = ImageMobject(filename_or_array="../assets/python-logo.png")
        nginx_icon_1 = SVGMobject(file_name="../assets/nginx-logo.svg")
        iis_icon_1 = SVGMobject(file_name="../assets/iis-logo.svg")

        python_icon_1.scale(0.3).align_to(virtual_machine_border_1, direction=UP + LEFT)
        python_icon_1.shift(DOWN * 1).shift(RIGHT * 0.5)

        nginx_icon_1.scale(0.5).align_to(virtual_machine_border_1, direction=UP + RIGHT)
        nginx_icon_1.shift(DOWN * 1).shift(LEFT * 0.5)

        iis_icon_1.add_background_rectangle(color=WHITE, opacity=1, buff=0.5)
        iis_icon_1.scale(0.2).align_to(virtual_machine_border_1, direction=UP + LEFT)
        iis_icon_1.shift(DOWN * 2).shift(RIGHT * 2)

        python_icon_2 = ImageMobject(filename_or_array="../assets/python-logo.png")
        nginx_icon_2 = SVGMobject(file_name="../assets/nginx-logo.svg")
        iis_icon_2 = SVGMobject(file_name="../assets/iis-logo.svg")

        python_icon_2.scale(0.3).align_to(virtual_machine_border_2, direction=UP + LEFT)
        python_icon_2.shift(DOWN * 1).shift(RIGHT * 0.5)

        nginx_icon_2.scale(0.5).align_to(virtual_machine_border_2, direction=UP + RIGHT)
        nginx_icon_2.shift(DOWN * 1).shift(LEFT * 0.5)

        iis_icon_2.add_background_rectangle(color=WHITE, opacity=1, buff=0.5)
        iis_icon_2.scale(0.2).align_to(virtual_machine_border_2, direction=UP + LEFT)
        iis_icon_2.shift(DOWN * 2).shift(RIGHT * 2)

        self.play(
            FadeIn(python_icon_1),
            FadeIn(nginx_icon_1),
            FadeIn(iis_icon_1),
            FadeIn(python_icon_2),
            FadeIn(nginx_icon_2),
            FadeIn(iis_icon_2),
        )

        self.next_slide()
        application_code_1 = SVGMobject(file_name="../assets/code-icon.svg").scale(0.7)
        application_code_1.align_to(virtual_machine_border_1, direction=DOWN + LEFT)
        application_code_1.shift(UP * 0.5, RIGHT * 2)

        application_code_2 = SVGMobject(file_name="../assets/code-icon.svg").scale(0.7)
        application_code_2.align_to(virtual_machine_border_2, direction=DOWN + LEFT)
        application_code_2.shift(UP * 0.5, RIGHT * 2)
        self.play(FadeIn(application_code_1), FadeIn(application_code_2))
        self.next_slide()


class ContainersDeployment(Slide):
    def construct(self):
        header_text = Text(text="Containers")
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()
        python_icon = ImageMobject(filename_or_array="../assets/python-logo.png")
        nginx_icon = SVGMobject(file_name="../assets/nginx-logo.svg")
        code_icon = SVGMobject(file_name="../assets/code-icon.svg")

        python_icon = python_icon.scale(0.3)
        nginx_icon = nginx_icon.scale(0.5)
        code_icon = code_icon.scale(0.4)

        nginx_icon.next_to(python_icon, DOWN, buff=0.5)
        code_icon.next_to(nginx_icon, DOWN, buff=0.5)

        dependencies_group = Group()
        dependencies_group.add(python_icon, nginx_icon, code_icon)

        dependencies_group.center()
        dependencies_group.to_edge(LEFT, buff=0.5)

        self.play(FadeIn(dependencies_group))

        self.next_slide()
        container_img_icon = SVGMobject("../assets/conatainer-img-icon.svg")
        container_img_icon.add(
            Text(text="Container Image")
            .next_to(container_img_icon, DOWN, buff=0.2)
            .scale(0.7)
        )
        container_img_icon = container_img_icon.scale(0.5)

        arrow_1 = Arrow(
            start=python_icon.get_edge_center(RIGHT),
            end=container_img_icon.get_edge_center(LEFT),
            buff=1.5,
            stroke_width=4,
            tip_length=0.2,
        )

        arrow_2 = Arrow(
            start=nginx_icon.get_edge_center(RIGHT),
            end=container_img_icon.get_edge_center(LEFT),
            buff=1.5,
            stroke_width=4,
            tip_length=0.2,
        )

        arrow_3 = Arrow(
            start=code_icon.get_edge_center(RIGHT),
            end=container_img_icon.get_edge_center(LEFT),
            buff=1.5,
            stroke_width=4,
            tip_length=0.2,
        )

        self.play(
            FadeIn(arrow_1),
            FadeIn(arrow_2),
            FadeIn(arrow_3),
            FadeIn(container_img_icon),
        )

        self.next_slide()
        container_icon_1 = SVGMobject(file_name="../assets/container-icon.svg").scale(
            0.5
        )
        container_icon_2 = SVGMobject(file_name="../assets/container-icon.svg").scale(
            0.5
        )
        container_icon_3 = SVGMobject(file_name="../assets/container-icon.svg").scale(
            0.5
        )

        container_icon_1.add(
            Text(text="Container 1")
            .scale(0.7)
            .next_to(container_icon_1, DOWN, buff=0.2)
        )
        container_icon_2.add(
            Text(text="Container 2")
            .scale(0.7)
            .next_to(container_icon_2, DOWN, buff=0.2)
        )
        container_icon_3.add(
            Text(text="Container 3")
            .scale(0.7)
            .next_to(container_icon_3, DOWN, buff=0.2)
        )

        container_icon_2.next_to(container_icon_1, DOWN, buff=1)
        container_icon_3.next_to(container_icon_2, DOWN, buff=1)

        containers_icon_group = Group()
        containers_icon_group.add(container_icon_1, container_icon_2, container_icon_3)
        containers_icon_group.center()
        containers_icon_group.to_edge(RIGHT, buff=0.5)

        arrow_4 = Arrow(
            start=container_img_icon.get_edge_center(RIGHT),
            end=container_icon_1.get_edge_center(LEFT),
            buff=1.0,
            stroke_width=4,
            tip_length=0.2,
        )

        arrow_5 = Arrow(
            start=container_img_icon.get_edge_center(RIGHT),
            end=container_icon_2.get_edge_center(LEFT),
            buff=1.0,
            stroke_width=4,
            tip_length=0.2,
        )

        arrow_6 = Arrow(
            start=container_img_icon.get_edge_center(RIGHT),
            end=container_icon_3.get_edge_center(LEFT),
            buff=1.0,
            stroke_width=4,
            tip_length=0.2,
        )

        self.play(FadeIn(arrow_4), FadeIn(container_icon_1))
        self.next_slide()
        self.play(FadeIn(arrow_5), FadeIn(container_icon_2))
        self.play(FadeIn(arrow_6), FadeIn(container_icon_3))


class VirtualMachineVsContainer(Slide):
    def construct(self):
        header_text = Text(text="Virtual Machines vs Containers")
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()
        container_stacking = ImageMobject(
            filename_or_array="../assets/container_under_the_hood.webp"
        )
        container_stacking.add(
            Text(text="Container").next_to(container_stacking, DOWN, buff=0.5)
        )
        container_stacking = container_stacking.scale(0.5)

        vm_stacking = ImageMobject(filename_or_array="../assets/vm_under_the_hood.webp")
        vm_stacking.add(
            Text(text="Virtual Machine").next_to(vm_stacking, DOWN, buff=0.5)
        )

        vm_stacking = vm_stacking.scale(0.5).next_to(container_stacking, LEFT, buff=3)

        group = Group()
        group.add(vm_stacking, container_stacking)
        group.center()

        self.play(FadeIn(vm_stacking))

        self.next_slide()
        self.play(FadeIn(container_stacking))

        source = Text(
            text="Source: https://www.docker.com/resources/what-container/"
        ).scale(0.5)
        source.to_edge(DOWN, buff=0.2)
        source.to_edge(RIGHT, buff=0.2)
        self.play(FadeIn(source))


class ProblemWithContainer(Slide):
    def construct(self):
        header_text = Text(text="Issues with containers").scale(0.7)
        header_text.to_edge(edge=UP)
        header_text.to_edge(edge=LEFT, buff=0.5)
        cursor = CURSOR.copy().scale(0.6).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()
        users_icon = SVGMobject(file_name="../assets/users-icon.svg")
        users_icon.add(
            Text(text="Users").scale(0.8).next_to(users_icon, DOWN, buff=0.2)
        )
        users_icon.center()
        users_icon.to_edge(LEFT, buff=0.2)
        users_icon.scale(0.4)

        self.play(FadeIn(users_icon))

        self.next_slide()
        server_border_1 = RoundedRectangle(
            width=10, height=6, stroke_width=1, corner_radius=0.1
        )
        server_border_1.to_edge(RIGHT)
        server_icon = SVGMobject("../assets/server-icon.svg")
        server_icon.scale(0.5).move_to(server_border_1.get_corner(UP + RIGHT))
        self.play(Create(server_border_1), FadeIn(server_icon))

        container_1 = SVGMobject(file_name="../assets/container-icon.svg").scale(0.5)
        container_1.move_to(server_border_1.get_center())
        self.play(FadeIn(container_1))

        self.next_slide()
        arrow_1 = Arrow(
            start=users_icon.get_edge_center(RIGHT),
            end=container_1.get_edge_center(LEFT),
            buff=1.0,
            stroke_width=4,
            tip_length=0.2,
        )

        self.play(GrowArrow(arrow_1))
        self.next_slide()

        container_2 = container_1.copy()
        container_2.next_to(container_1, DOWN, buff=0.5)
        container_group_1 = Group(container_1, container_2)
        self.play(FadeIn(container_2))
        self.play(container_group_1.animate.move_to(server_border_1.get_center()))
        self.next_slide()

        question_mark_text = Text(text="?", color=RED)
        question_mark_text.move_to(arrow_1.get_tip())
        question_mark_text.shift(UP * 0.5)
        self.play(FadeIn(question_mark_text))

        self.next_slide()

        self.play(FadeOut(question_mark_text), FadeOut(arrow_1))

        self.play(
            server_border_1.animate.stretch_to_fit_width(7, about_edge=RIGHT),
            server_border_1.animate.stretch_to_fit_height(3, about_edge=UP),
        )

        self.play(container_group_1.animate.move_to(server_border_1.get_center()))

        server_border_2 = server_border_1.copy()
        server_border_2.next_to(server_border_1, DOWN, buff=0.5)
        server_icon_2 = server_icon.copy()
        server_icon_2.move_to(server_border_2.get_corner(UP + RIGHT))
        self.play(Create(server_border_2), FadeIn(server_icon_2))

        container_group_2 = container_group_1.copy()
        container_group_2.move_to(server_border_2.get_center())
        self.play(FadeIn(container_group_2))

        self.next_slide()
        question_mark_text.next_to(users_icon, RIGHT, buff=0.5)
        self.play(FadeIn(question_mark_text))


class KubernetesLogo(Slide):
    def construct(self):
        k8s_logo = SVGMobject(file_name="../assets/k8s_logo.svg")
        k8s_logo.add(
            Text(text="Kubernetes").scale(1.5).next_to(k8s_logo, RIGHT, buff=0.2)
        )
        k8s_logo.center()
        self.play(FadeIn(k8s_logo))


class KubernetesOverview(Slide):
    def construct(self):
        header_text = Text(text="How to solve this problem?").scale(0.7)
        header_text.to_edge(edge=UP)
        header_text.to_edge(edge=LEFT, buff=0.5)
        self.add(header_text)
        self.play(FadeIn(header_text))
        self.next_slide()

        users_icon = SVGMobject(file_name="../assets/users-icon.svg")
        users_icon.add(
            Text(text="Users").scale(0.8).next_to(users_icon, DOWN, buff=0.2)
        )
        users_icon.center()
        users_icon.to_edge(LEFT, buff=0.2)
        users_icon.scale(0.4)

        self.add(users_icon)
        self.play(FadeIn(users_icon))
        self.next_slide()

        server_border_1 = RoundedRectangle(
            width=7, height=3, stroke_width=1, corner_radius=0.1
        )
        server_border_1.to_edge(RIGHT)
        server_border_1.shift(UP * 1.5)
        server_icon = SVGMobject("../assets/server-icon.svg")
        server_icon.scale(0.5).move_to(server_border_1.get_corner(UP + RIGHT))
        self.add(server_border_1, server_icon)

        container_1 = SVGMobject(file_name="../assets/container-icon.svg").scale(0.5)
        container_1.move_to(server_border_1.get_center())
        container_2 = container_1.copy()
        container_2.next_to(container_1, DOWN, buff=0.5)
        container_group_1 = Group(container_1, container_2)

        container_group_1.move_to(server_border_1.get_center())
        self.add(container_group_1)

        server_border_2 = server_border_1.copy()
        server_border_2.next_to(server_border_1, DOWN, buff=0.5)
        server_icon_2 = server_icon.copy()
        server_icon_2.move_to(server_border_2.get_corner(UP + RIGHT))
        self.add(server_border_2, server_icon_2)

        container_group_2 = container_group_1.copy()
        container_group_2.move_to(server_border_2.get_center())
        self.add(container_group_2)

        self.play(
            Create(server_border_1),
            GrowFromCenter(server_icon),
            FadeIn(container_group_1),
            Create(server_border_2),
            GrowFromCenter(server_icon_2),
            FadeIn(container_group_2),
        )
        self.next_slide()

        server_border_3 = RoundedRectangle(
            width=2, height=2, stroke_width=1, corner_radius=0.1
        )

        server_border_3.next_to(users_icon, RIGHT, buff=2)
        server_icon_3 = server_icon.copy()
        server_icon_3.move_to(server_border_3.get_corner(UP + RIGHT))
        self.add(server_border_3)
        self.add(server_icon_3)

        self.play(Create(server_border_3), GrowFromCenter(server_icon_3))
        self.next_slide()

        arrow_user_server_3 = Arrow(
            start=users_icon.get_edge_center(RIGHT),
            end=server_border_3.get_edge_center(LEFT),
            stroke_width=4,
            tip_length=0.2,
        )
        self.add(arrow_user_server_3)
        self.play(GrowArrow(arrow_user_server_3))

        arrow_server_3_server_1 = Arrow(
            start=server_border_3.get_edge_center(RIGHT),
            end=server_border_1.get_center(),
            stroke_width=4,
            tip_length=0.2,
            buff=1,
        )
        self.add(arrow_server_3_server_1)
        self.play(GrowArrow(arrow_server_3_server_1))

        arrow_server_3_server_2 = Arrow(
            start=server_border_3.get_edge_center(RIGHT),
            end=server_border_2.get_center(),
            stroke_width=4,
            tip_length=0.2,
            buff=1,
        )
        self.add(arrow_server_3_server_2)
        self.play(GrowArrow(arrow_server_3_server_2))
        self.next_slide()

        cross = Cross().scale_to_fit_width(container_1.width)
        cross.move_to(container_1.get_center()).shift(DOWN * 0.2)
        self.add(cross)
        self.play(FadeIn(cross))
        self.next_slide()

        container_3 = container_1.copy()
        container_3.move_to(server_border_2.get_center())
        container_3.shift(RIGHT * 2)
        self.add(container_3)
        self.play(FadeIn(container_3))
        self.play(Circumscribe(container_3))
        self.next_slide()

        kubernetes_logo = (
            SVGMobject(file_name="../assets/k8s_logo.svg")
            .scale_to_fit_width(server_border_3.width)
            .scale(0.5)
        )
        kubernetes_logo.move_to(server_border_3.get_center())
        self.add(kubernetes_logo)
        self.play(FadeIn(kubernetes_logo))


class KubernetesHowItWorks(Slide):
    def construct(self):
        header_text = Text(text="How Kubernetes Works?").scale(0.7)
        header_text.to_edge(edge=UP)
        self.add(header_text)
        self.play(FadeIn(header_text))

        self.next_slide()
        server_border_1 = RoundedRectangle(
            width=7, height=3, stroke_width=1, corner_radius=0.1
        )
        server_border_1.to_edge(RIGHT)
        server_border_1.shift(UP * 1.5)
        server_icon = SVGMobject("../assets/server-icon.svg")
        server_icon.scale(0.5).move_to(server_border_1.get_corner(UP + RIGHT))
        self.add(server_border_1, server_icon)

        server_border_2 = server_border_1.copy()
        server_border_2.next_to(server_border_1, DOWN, buff=0.5)
        server_icon_2 = server_icon.copy()
        server_icon_2.move_to(server_border_2.get_corner(UP + RIGHT))
        self.add(server_border_2, server_icon_2)
        self.play(
            Create(server_border_1),
            GrowFromCenter(server_icon),
            Create(server_border_2),
            GrowFromCenter(server_icon_2),
        )

        server_border_3 = RoundedRectangle(
            width=3, height=3, stroke_width=1, corner_radius=0.1
        )

        server_border_3.to_edge(LEFT, buff=1)
        server_icon_3 = server_icon.copy()
        server_icon_3.move_to(server_border_3.get_corner(UP + RIGHT))
        self.add(server_border_3)
        self.add(server_icon_3)

        self.play(Create(server_border_3), GrowFromCenter(server_icon_3))

        self.next_slide()
        control_plane_text = Text(text="Control Plane (Master)").scale(0.5)
        control_plane_text.next_to(
            server_border_3.get_edge_center(DOWN), DOWN, buff=0.2
        )
        self.add(control_plane_text)
        self.play(FadeIn(control_plane_text))
        self.next_slide()

        worker_text_1 = Text(text="Worker 1").scale(0.5)
        worker_text_1.next_to(server_border_1.get_edge_center(UP), DOWN, buff=0.2)

        worker_text_2 = Text(text="Worker 2").scale(0.5)
        worker_text_2.next_to(server_border_2.get_edge_center(UP), DOWN, buff=0.2)

        self.add(worker_text_1, worker_text_2)
        self.play(FadeIn(worker_text_1), FadeIn(worker_text_2))
        self.next_slide()

        k8s_scheduler = ImageMobject(filename_or_array="../assets/k8s_scheduler.png")
        k8s_api = ImageMobject(filename_or_array="../assets/k8s_api.png")
        k8s_proxy = ImageMobject(filename_or_array="../assets/k8s_proxy.png")
        k8s_kubelet = ImageMobject(filename_or_array="../assets/k8s_kubelet.png")

        k8s_scheduler.next_to(server_border_3.get_edge_center(UP), DOWN, buff=0.3)
        k8s_api.next_to(k8s_scheduler, DOWN, buff=0.5)

        self.add(k8s_scheduler, k8s_api)
        self.play(FadeIn(k8s_scheduler), FadeIn(k8s_api))
        self.next_slide()

        server_1_proxy_icon = k8s_proxy.copy().move_to(
            server_border_1.get_corner(UL) + DOWN * 0.7 + RIGHT * 1
        )
        server_1_kubelet_icon = k8s_kubelet.copy().next_to(
            server_1_proxy_icon, DOWN, buff=0.5
        )
        self.add(server_1_proxy_icon, server_1_kubelet_icon)
        self.play(FadeIn(server_1_proxy_icon), FadeIn(server_1_kubelet_icon))

        server_2_proxy_icon = k8s_proxy.copy().move_to(
            server_border_2.get_corner(UL) + DOWN * 0.7 + RIGHT * 1
        )
        server_2_kubelet_icon = k8s_kubelet.copy().next_to(
            server_2_proxy_icon, DOWN, buff=0.5
        )
        self.add(server_2_proxy_icon, server_2_kubelet_icon)
        self.play(FadeIn(server_2_proxy_icon), FadeIn(server_2_kubelet_icon))
        self.next_slide()

        arrow_server_3_server_1 = Arrow(
            start=server_border_3.get_edge_center(RIGHT),
            end=server_border_1.get_edge_center(LEFT),
            stroke_width=4,
            tip_length=0.2,
            buff=0.5,
        )
        arrow_server_3_server_2 = Arrow(
            start=server_border_3.get_edge_center(RIGHT),
            end=server_border_2.get_edge_center(LEFT),
            stroke_width=4,
            tip_length=0.2,
            buff=0.5,
        )
        self.add(arrow_server_3_server_1, arrow_server_3_server_2)
        self.play(
            GrowArrow(arrow_server_3_server_1), GrowArrow(arrow_server_3_server_2)
        )
        self.next_slide()

        python_icon_1 = ImageMobject(filename_or_array="../assets/python-logo.png")
        python_icon_1.scale(0.3).next_to(worker_text_1, DOWN, buff=0.5)
        python_icon_2 = ImageMobject(filename_or_array="../assets/python-logo.png")
        python_icon_2.scale(0.3).next_to(worker_text_2, DOWN, buff=0.5)
        angular_icon_1 = SVGMobject(file_name="../assets/angular-logo.svg")
        angular_icon_1.scale(0.5).next_to(python_icon_2, RIGHT, buff=0.7)
        self.add(python_icon_1, python_icon_2, angular_icon_1)
        self.play(FadeIn(python_icon_1), FadeIn(python_icon_2), FadeIn(angular_icon_1))
        self.next_slide()


class KubernetesComponent(Slide):
    def construct(self):
        header_text = Text(text="K8s - The basic concepts").scale(0.7)
        header_text.to_edge(edge=UP + LEFT)
        self.add(header_text)
        self.play(FadeIn(header_text))
        self.next_slide()

        server_border_1 = RoundedRectangle(
            width=7, height=3, stroke_width=1, corner_radius=0.1
        )
        server_border_1.to_edge(RIGHT)
        server_border_1.shift(UP * 1.5)
        server_icon = SVGMobject("../assets/server-icon.svg")
        server_icon.scale(0.5).move_to(server_border_1.get_corner(UP + RIGHT))
        self.add(server_border_1, server_icon)

        server_border_2 = server_border_1.copy()
        server_border_2.next_to(server_border_1, DOWN, buff=0.5)
        server_icon_2 = server_icon.copy()
        server_icon_2.move_to(server_border_2.get_corner(UP + RIGHT))
        self.add(server_border_2, server_icon_2)

        server_border_3 = RoundedRectangle(
            width=3, height=3, stroke_width=1, corner_radius=0.1
        )

        server_border_3.to_edge(LEFT, buff=1)
        server_icon_3 = server_icon.copy()
        server_icon_3.move_to(server_border_3.get_corner(UP + RIGHT))
        self.add(server_border_3)
        self.add(server_icon_3)

        control_plane_text = Text(text="Control Plane (Master)").scale(0.5)
        control_plane_text.next_to(
            server_border_3.get_edge_center(DOWN), DOWN, buff=0.2
        )
        self.add(control_plane_text)

        worker_text_1 = Text(text="Worker 1").scale(0.5)
        worker_text_1.next_to(server_border_1.get_edge_center(UP), DOWN, buff=0.2)

        worker_text_2 = Text(text="Worker 2").scale(0.5)
        worker_text_2.next_to(server_border_2.get_edge_center(UP), DOWN, buff=0.2)

        self.add(worker_text_1, worker_text_2)

        k8s_scheduler = ImageMobject(filename_or_array="../assets/k8s_scheduler.png")
        k8s_api = ImageMobject(filename_or_array="../assets/k8s_api.png")
        k8s_proxy = ImageMobject(filename_or_array="../assets/k8s_proxy.png")
        k8s_kubelet = ImageMobject(filename_or_array="../assets/k8s_kubelet.png")

        k8s_scheduler.next_to(server_border_3.get_edge_center(UP), DOWN, buff=0.3)
        k8s_api.next_to(k8s_scheduler, DOWN, buff=0.5)

        self.add(k8s_scheduler, k8s_api)

        server_1_proxy_icon = k8s_proxy.copy().move_to(
            server_border_1.get_corner(UL) + DOWN * 0.7 + RIGHT * 1
        )
        server_1_kubelet_icon = k8s_kubelet.copy().next_to(
            server_1_proxy_icon, DOWN, buff=0.5
        )
        self.add(server_1_proxy_icon, server_1_kubelet_icon)

        server_2_proxy_icon = k8s_proxy.copy().move_to(
            server_border_2.get_corner(UL) + DOWN * 0.7 + RIGHT * 1
        )
        server_2_kubelet_icon = k8s_kubelet.copy().next_to(
            server_2_proxy_icon, DOWN, buff=0.5
        )
        self.add(server_2_proxy_icon, server_2_kubelet_icon)

        arrow_server_3_server_1 = Arrow(
            start=server_border_3.get_edge_center(RIGHT),
            end=server_border_1.get_edge_center(LEFT),
            stroke_width=4,
            tip_length=0.2,
            buff=0.5,
        )
        arrow_server_3_server_2 = Arrow(
            start=server_border_3.get_edge_center(RIGHT),
            end=server_border_2.get_edge_center(LEFT),
            stroke_width=4,
            tip_length=0.2,
            buff=0.5,
        )
        self.add(arrow_server_3_server_1, arrow_server_3_server_2)

        python_icon_1 = ImageMobject(filename_or_array="../assets/python-logo.png")
        python_icon_1.scale(0.3).next_to(worker_text_1, DOWN, buff=0.5)
        python_icon_2 = ImageMobject(filename_or_array="../assets/python-logo.png")
        python_icon_2.scale(0.3).next_to(worker_text_2, DOWN, buff=0.5)
        angular_icon_1 = SVGMobject(file_name="../assets/angular-logo.svg")
        angular_icon_1.scale(0.5).next_to(python_icon_2, RIGHT, buff=0.7)
        self.add(python_icon_1, python_icon_2, angular_icon_1)
        self.next_slide()

        self.play(
            header_text.animate.become(
                Text(text="K8s - The Nodes").scale(0.7).to_edge(UP + LEFT)
            )
        )
        self.next_slide(loop=True)

        self.play(
            ShowPassingFlash(
                server_border_1.copy().set_stroke(width=5, color=RED),
                run_time=2,
                time_width=2.5,
            ),
            ShowPassingFlash(
                server_border_2.copy().set_stroke(width=5, color=RED),
                run_time=2,
                time_width=2.5,
            ),
            ShowPassingFlash(
                server_border_3.copy().set_stroke(width=5, color=RED),
                run_time=2,
                time_width=2.5,
            ),
        )

        self.next_slide()
        self.play(
            header_text.animate.become(
                Text(text="K8s - The Pods").scale(0.7).to_edge(UP + LEFT)
            )
        )

        self.next_slide(loop=True)
        self.play(
            Circumscribe(
                python_icon_1,
                time_width=2.5,
                color=RED,
                shape=Circle,
                buff=0.1,
                run_time=2,
            ),
            Circumscribe(
                python_icon_2,
                time_width=2.5,
                color=RED,
                shape=Circle,
                buff=0.1,
                run_time=2,
            ),
            Circumscribe(
                angular_icon_1,
                time_width=2.5,
                color=RED,
                shape=Circle,
                buff=0.1,
                run_time=2,
            ),
            Circumscribe(
                server_1_proxy_icon,
                time_width=2.5,
                color=RED,
                shape=Circle,
                buff=0.1,
                run_time=2,
            ),
            Circumscribe(
                server_2_proxy_icon,
                time_width=2.5,
                color=RED,
                shape=Circle,
                buff=0.1,
                run_time=2,
            ),
            Circumscribe(
                server_1_kubelet_icon,
                time_width=2.5,
                color=RED,
                shape=Circle,
                buff=0.1,
                run_time=2,
            ),
            Circumscribe(
                server_2_kubelet_icon,
                time_width=2.5,
                color=RED,
                shape=Circle,
                buff=0.1,
                run_time=2,
            ),
            Circumscribe(
                k8s_api, time_width=2.5, color=RED, shape=Circle, buff=0.1, run_time=2
            ),
            Circumscribe(
                k8s_scheduler,
                time_width=2.5,
                color=RED,
                shape=Circle,
                buff=0.1,
                run_time=2,
            ),
        )

        self.next_slide()
        self.play(
            header_text.animate.become(
                Text(text="K8s - The Namespaces").scale(0.7).to_edge(UP + LEFT)
            )
        )

        kube_system_server_1 = Group(server_1_proxy_icon, server_1_kubelet_icon)
        kube_system_server_2 = Group(server_2_proxy_icon, server_2_kubelet_icon)
        kube_system_server_3 = Group(k8s_scheduler, k8s_api)
        user_namespace = Group(python_icon_1, python_icon_2, angular_icon_1)

        bounding_box_kube_system_1 = SurroundingRectangle(
            kube_system_server_1, buff=0.1, color=BLUE, corner_radius=0.1
        )
        bounding_box_kube_system_2 = SurroundingRectangle(
            kube_system_server_2, buff=0.1, color=BLUE, corner_radius=0.1
        )
        bounding_box_kube_system_3 = SurroundingRectangle(
            kube_system_server_3, buff=0.1, color=BLUE, corner_radius=0.1
        )
        bounding_box_user_namespace = SurroundingRectangle(
            user_namespace, buff=0.1, color=RED, corner_radius=0.1
        )
        self.play(
            Create(bounding_box_kube_system_1),
            Create(bounding_box_kube_system_2),
            Create(bounding_box_kube_system_3),
            Create(bounding_box_user_namespace),
        )

        self.next_slide()
        self.play(
            header_text.animate.become(
                Text(text="K8s - The Deployment").scale(0.7).to_edge(UP + LEFT)
            )
        )

        self.play(
            FadeOut(bounding_box_kube_system_1),
            FadeOut(bounding_box_kube_system_2),
            FadeOut(bounding_box_kube_system_3),
            FadeOut(bounding_box_user_namespace),
        )

        self.next_slide()
        bounding_box_backend_deployment = SurroundingRectangle(
            Group(python_icon_1, python_icon_2), buff=0.1, color=BLUE, corner_radius=0.1
        )
        bounding_box_front_end_deployment = SurroundingRectangle(
            Group(angular_icon_1), buff=0.1, color=RED, corner_radius=0.1
        )
        self.play(
            Create(bounding_box_backend_deployment),
            Create(bounding_box_front_end_deployment),
        )

        self.next_slide()
        self.play(
            header_text.animate.become(
                Text(text="K8s - The Services & The Ingress")
                .scale(0.7)
                .to_edge(UP + LEFT)
            )
        )

        k8s_ingress = ImageMobject(filename_or_array="../assets/k8s_ingress.png")
        k8s_ingress.add(
            Text(text="Ingress").scale(0.5).next_to(k8s_ingress, DOWN, buff=0.2)
        )
        k8s_ingress.next_to(control_plane_text, DOWN, buff=0.2)
        self.add(k8s_ingress)
        self.play(FadeIn(k8s_ingress))

        ingress_to_backend_arrow = CurvedArrow(
            k8s_ingress.get_corner(UP + RIGHT),
            bounding_box_backend_deployment.get_corner(UP + LEFT),
            angle=-PI / 2,
            tip_length=0.2,
        ).set_stroke(width=3, color=BLUE)
        ingress_to_frontend_arrow = CurvedArrow(
            k8s_ingress.get_corner(DOWN + RIGHT),
            bounding_box_front_end_deployment.get_corner(DOWN + LEFT),
            angle=PI / 5,
            tip_length=0.2,
        ).set_stroke(width=3, color=RED)
        self.add(ingress_to_frontend_arrow)
        self.add(ingress_to_backend_arrow)
        self.next_slide(loop=True)
        self.play(
            Create(ingress_to_frontend_arrow, run_time=2),
            Create(ingress_to_backend_arrow, run_time=2),
        )
        self.next_slide()


class Demo(Slide):
    def construct(self):
        header_text = Text(text="Demo").scale(1.2)
        header_text.center()
        self.add(header_text)
        self.play(FadeIn(header_text))

        self.next_slide()


class K8sOnDifferentCloudProviders(Slide):
    def construct(self):
        header_text = Text(text="Kubernetes on Different Cloud Providers").scale(0.7)
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()

        icons_group = Group()

        eks_logo = ImageMobject(filename_or_array="../assets/eks_logo.png")
        eks_text = Text(text="Amazon EKS")
        eks_logo.add(eks_text.next_to(eks_logo, DOWN, buff=0.5))
        eks_logo.scale(0.4)

        aks_logo = ImageMobject(filename_or_array="../assets/aks_logo.png")
        aks_text = Text(text="Azure AKS")
        aks_logo.add(aks_text.next_to(aks_logo, DOWN, buff=0.5))
        aks_logo.scale_to_fit_height(eks_logo.height)
        aks_logo.next_to(eks_logo, RIGHT, buff=2)

        gke_logo = ImageMobject(filename_or_array="../assets/gke_logo.png")
        gke_text = Text(text="Google GKE")
        gke_logo.add(gke_text.next_to(gke_logo, DOWN, buff=0.5))
        gke_logo.scale_to_fit_height(aks_logo.height)
        gke_logo.next_to(aks_logo, RIGHT, buff=2)

        icons_group.add(eks_logo, aks_logo, gke_logo)
        icons_group.center()

        self.play(FadeIn(eks_logo))

        self.next_slide()
        self.play(FadeIn(aks_logo))

        self.next_slide()
        self.play(FadeIn(gke_logo))


class K8sVersusCloudNativeServices(Slide):
    def construct(self):
        header_text = Text(text="Kubernetes vs PaaS/FaaS").scale(0.7)
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()

        comparison_table = ImageMobject(
            filename_or_array="../assets/k8s_vs_PaaSFaaS.png"
        )
        comparison_table.scale(1.5)
        comparison_table.next_to(header_text, DOWN, buff=0)
        self.add(comparison_table)
        self.play(FadeIn(comparison_table))

        self.next_slide()


class ResourcesUsedInSlides(Slide):
    def construct(self):
        header_text = Text(text="Resources Used in Slides").scale(0.7)
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()

        icons_group = Group()

        github_demo_qr_code = ImageMobject(
            filename_or_array="../assets/github_demo_qr_code.png"
        )
        github_qr_code_text = Text(text="Demo Source Code")
        github_demo_qr_code.add(
            github_qr_code_text.next_to(github_demo_qr_code, DOWN, buff=0.5)
        )

        notion_qr_code = ImageMobject(filename_or_array="../assets/notion_qr_code.png")
        notion_qr_text = Text(text="Tutorial Notes")
        notion_qr_code.add(notion_qr_text.next_to(notion_qr_code, DOWN, buff=0.5))
        notion_qr_code.scale_to_fit_height(github_demo_qr_code.height)
        notion_qr_code.next_to(github_demo_qr_code, RIGHT, buff=2)

        icons_group.add(github_demo_qr_code, notion_qr_code)
        icons_group.center()

        self.play(FadeIn(github_demo_qr_code))

        self.next_slide()

        self.play(FadeIn(notion_qr_code))

        self.next_slide()


class OtherUsefulResources(Slide):
    # TODO: Add other useful resources
    def construct(self):
        header_text = Text(text="Other Useful Resources").scale(0.7)
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()

        resources = Text(text="Resources:").scale(0.5)
        resources.next_to(header_text, direction=DOWN, buff=1)
        self.play(FadeIn(resources))

        self.next_slide()

        resource_list = [
            "https://kubernetes.io/docs/concepts/",
            "https://www.docker.com/resources/what-container/",
            "https://www.youtube.com/watch?v=PH-2FfFD2PU",
            "https://www.youtube.com/watch?v=4ht22ReBjno",
        ]

        for resource in resource_list:
            resource_text = Text(text=resource).scale(0.5)
            resource_text.next_to(resources, DOWN, buff=0.2)
            resources.add(resource_text)
            self.play(FadeIn(resource_text))


class FeedbackForm(Slide):
    # TODO: Add QR code for feedback form
    def construct(self):
        header_text = Text(text="We would love to hear your feedback!").scale(0.7)
        header_text.to_edge(edge=UP)
        cursor = CURSOR.copy().scale(0.8).move_to(header_text[0])  # Position the cursor
        self.add(header_text)
        self.play(
            TypeWithCursor(
                text=header_text,
                cursor=cursor,
                leave_cursor_on=False,
                time_per_char=0.05,
            )
        )

        self.next_slide()

        github_demo_qr_code = ImageMobject(
            filename_or_array="../assets/github_demo_qr_code.png"
        )
        github_demo_qr_code.scale(1.5)

        github_demo_qr_code.next_to(header_text, DOWN, buff=1)
        self.play(FadeIn(github_demo_qr_code))
        self.next_slide()
