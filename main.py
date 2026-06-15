import flet as ft
import os


def main(page: ft.Page):
    page.title = "Wilhelm Wilson Shipandeni Moses | Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    page.bgcolor = "#F5F7FA"

    # ── helpers ──────────────────────────────────────────────────────────────
    def section(title, *children):
        return ft.Container(
            content=ft.Column(
                [ft.Text(title, size=24, weight=ft.FontWeight.BOLD, color="#0A2E5C")]
                + list(children),
                spacing=10,
            ),
            bgcolor="white",
            padding=20,
            border_radius=15,
        )

    def divider():
        return ft.Divider(color="#E0E7FF")

    # ── WELCOME ───────────────────────────────────────────────────────────────
    welcome = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Welcome to My Personal Portfolio",
                    size=34,
                    weight=ft.FontWeight.BOLD,
                    color="#0A2E5C",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Mining Engineering Student  |  Lead Developer Assistant  |  Future Engineer",
                    size=17,
                    text_align=ft.TextAlign.CENTER,
                    color="#374151",
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#E8F0FE",
        padding=30,
        border_radius=15,
    )

    # ── PROFILE IMAGE ─────────────────────────────────────────────────────────
    profile = (
        ft.Image(src="profile.jpg", width=180, height=180, border_radius=90,
                 fit=ft.BoxFit.COVER)
        if os.path.exists("assets/profile.jpg")
        else ft.Icon(ft.Icons.PERSON, size=180)
    )

    # ── HEADER ────────────────────────────────────────────────────────────────
    header = ft.Container(
        content=ft.Row(
            [
                profile,
                ft.Column(
                    [
                        ft.Text("Wilhelm Wilson Shipandeni Moses", size=28,
                                weight=ft.FontWeight.BOLD, color="#0A2E5C"),
                        ft.Text("Student Number: 224096389", color="#374151"),
                        ft.Text("Mining Engineering Student", size=16, color="#374151"),
                        ft.Text("Lead Developer Assistant – QuoteWise", color="#374151"),
                        ft.Text("University of Namibia (UNAM)", color="#374151"),
                        ft.Text("JEDS Campus – Ongwediva, Namibia", color="#374151"),
                    ],
                    spacing=4,
                ),
            ],
            spacing=20,
        ),
        bgcolor="white",
        padding=20,
        border_radius=15,
    )

    # ── ABOUT ─────────────────────────────────────────────────────────────────
    about = section(
        "About Me",
        ft.Text(
            "My name is Wilhelm Wilson Shipandeni Moses and I am a Mining Engineering "
            "student at the University of Namibia.\n\n"
            "I am passionate about engineering, technology and software development. "
            "During Computer Programming I, I contributed to the development of the "
            "QuoteWise mobile application as a Lead Developer Assistant.\n\n"
            "Outside academics I enjoy playing video games and watching football.\n\n"
            "My goal is to combine engineering and software development skills to create "
            "innovative solutions for the mining and construction industries.",
            color="#374151",
        ),
    )

    # ── SKILLS ───────────────────────────────────────────────────────────────
    skill_items = [
        "• AutoCAD", "• MATLAB", "• Python Programming",
        "• Flet Development", "• Welding", "• Machining", "• Bricklaying",
    ]
    skills = section("Skills", *[ft.Text(s, color="#374151") for s in skill_items])

    # ── STATS ─────────────────────────────────────────────────────────────────
    def stat_box(number, label, color):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(number, size=40, weight=ft.FontWeight.BOLD, color="white",
                            text_align=ft.TextAlign.CENTER),
                    ft.Text(label, color="white", text_align=ft.TextAlign.CENTER, size=13),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
            ),
            expand=True,
            bgcolor=color,
            padding=20,
            border_radius=12,
        )

    stats = ft.Row(
        [
            stat_box("8", "MATLAB Courses Completed", "#00897B"),
            stat_box("1", "Major Team Project", "#E64A19"),
            stat_box("7+", "Technical Skills", "#6A1B9A"),
        ],
        spacing=12,
    )

    # ── QUOTEWISE ────────────────────────────────────────────────────────────
    responsibilities = [
        "Assisting with project planning",
        "Participating in feature discussions",
        "Supporting software testing activities",
        "Identifying and reporting bugs",
        "Assisting with debugging",
        "Reviewing user interface designs",
        "Coordinating development activities",
        "Contributing ideas to improve user experience",
    ]

    screenshots = ft.Column(
        [
            ft.Image(src=f"screenshot{i}.png", width=900, height=450)
            for i in range(1, 7)
            if os.path.exists(f"assets/screenshot{i}.png")
        ],
        spacing=14,
    )

    quotewise = section(
        "QuoteWise Mobile Application",
        ft.Container(
            content=ft.Text(
                "QuoteWise connects construction companies with clients — enabling companies to "
                "showcase services while clients compare providers and find suitable contractors.",
                color="white",
            ),
            bgcolor="#1565C0", padding=14, border_radius=10,
        ),
        ft.Text("Role: Lead Developer Assistant", size=16,
                weight=ft.FontWeight.BOLD, color="#E64A19"),
        ft.Text("Responsibilities:", weight=ft.FontWeight.BOLD, color="#374151"),
        *[ft.Text(f"  ✓  {r}", color="#374151") for r in responsibilities],
        divider(),
        ft.Text("QuoteWise Evidence Screenshots", size=16,
                weight=ft.FontWeight.BOLD, color="#0A2E5C"),
        screenshots,
    )

    # ── MATLAB ────────────────────────────────────────────────────────────────
    cert_names = [
        "MATLAB Onramp", "Machine Learning Onramp", "Deep Learning Onramp",
        "Computer Vision Onramp", "Signal Processing Onramp",
        "Statistics Onramp", "Image Processing Onramp", "Simulink Onramp",
    ]
    matlab = section(
        "MATLAB Achievement Hub",
        ft.Container(
            content=ft.Text(
                "Successfully completed 8 MathWorks self-paced courses. "
                "Click any certificate below to view or download.",
                color="white",
            ),
            bgcolor="#E64A19", padding=14, border_radius=10,
        ),
        *[
            ft.TextButton(f"📜  {cert_names[i]}", url=f"cert{i+1}.pdf")
            for i in range(8)
        ],
    )

    # ── TECHNICAL BLOG + EMBEDDED VIDEO ──────────────────────────────────────
    blog_posts = [
        ("Variables and Data Types",
         "Variables store information in memory; data types define how that information "
         "is represented and manipulated."),
        ("Functions in Python",
         "Functions allow developers to reuse code, improve organisation and reduce duplication."),
        ("Loops",
         "Loops automate repetitive tasks and improve efficiency when processing data."),
        ("Conditional Statements",
         "Conditional statements help programs make decisions based on different situations."),
        ("Event Driven Programming",
         "Event driven programming enables applications to respond to user actions "
         "such as button clicks and form submissions."),
        ("Flet Development",
         "Flet allows developers to create modern desktop, web and mobile applications using Python."),
    ]

    blog_entries = []
    for title, body in blog_posts:
        blog_entries += [
            ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color="#0A2E5C"),
            ft.Text(body, color="#374151"),
            divider(),
        ]

    # Video section — video file served directly from Flet assets (same domain)
    video_block = ft.Container(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.PLAY_CIRCLE_FILLED, size=48, color="#E64A19"),
                ft.Text(
                    "Individual Contribution Video",
                    size=18, weight=ft.FontWeight.BOLD, color="#0A2E5C",
                ),
                ft.Text(
                    "Click the button below to watch my individual contribution and "
                    "reflection video for the QuoteWise project. "
                    "The video opens in your browser's built-in player.",
                    color="#374151", text_align=ft.TextAlign.CENTER,
                ),
                ft.ElevatedButton(
                    "▶  Play Reflection Video",
                    bgcolor="#E64A19",
                    color="white",
                    url="reflection.mp4",
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        bgcolor="#FFF3E0",
        padding=24,
        border_radius=14,
    )

    blog = section(
        "Technical Blog",
        *blog_entries,
        ft.Text("Reflection Video (Individual Contribution)", size=18,
                weight=ft.FontWeight.BOLD, color="#0A2E5C"),
        video_block,
    )

    # ── GITHUB EVIDENCE ───────────────────────────────────────────────────────
    github = section(
        "GitHub Evidence",
        ft.Text(
            "The screenshot below provides evidence of my GitHub participation "
            "and contribution to the QuoteWise project.",
            color="#374151",
        ),
        ft.Image(src="github1.png", width=900)
        if os.path.exists("assets/github1.png")
        else ft.Text("GitHub screenshot not found.", color="#9CA3AF"),
    )

    # ── REFLECTION ────────────────────────────────────────────────────────────
    challenges = [
        ("Challenge 1: Team Coordination",
         "Working with a large development team required effective communication.",
         "Regular discussions and planning meetings ensured all members stayed aligned."),
        ("Challenge 2: Debugging and Error Resolution",
         "Several bugs and unexpected behaviours were encountered during development.",
         "Systematic testing and code reviews helped resolve issues efficiently."),
        ("Challenge 3: Time Management",
         "Balancing academic responsibilities with project deadlines was challenging.",
         "Task prioritisation and proper scheduling ensured milestones were met."),
        ("Challenge 4: User Interface Improvements",
         "Creating an intuitive interface required multiple revisions.",
         "Continuous testing and team feedback improved usability and user experience."),
    ]

    challenge_rows = []
    for title, problem, solution in challenges:
        challenge_rows += [
            ft.Text(title, weight=ft.FontWeight.BOLD, color="#0A2E5C"),
            ft.Text(problem, color="#374151"),
            ft.Text(f"Solution: {solution}", color="#374151"),
            divider(),
        ]

    reflection = section(
        "Reflection and Challenges Encountered",
        ft.Text(
            "The QuoteWise project provided valuable practical experience in software "
            "development and teamwork. As a Lead Developer Assistant, I contributed to "
            "planning, testing, debugging, interface evaluation, and coordination activities "
            "throughout the project lifecycle.\n\n"
            "The experience strengthened my technical skills, communication abilities and "
            "understanding of collaborative software development processes. Additionally, "
            "completing MATLAB training courses improved my computational and analytical "
            "skills, complementing my engineering studies.\n\n"
            "Overall, this semester enhanced my confidence in programming and demonstrated "
            "how software solutions can address real-world engineering challenges.",
            color="#374151",
        ),
        divider(),
        *challenge_rows,
    )

    # ── CONTACT ───────────────────────────────────────────────────────────────
    contact = section(
        "Contact Information",
        ft.TextButton("📧  moseswilhelm66@gmail.com", url="mailto:moseswilhelm66@gmail.com"),
        ft.TextButton("📸  Instagram — @the_african_nightmare",
                      url="https://www.instagram.com/the_african_nightmare"),
        ft.TextButton("💻  GitHub — the-african-nightmare66",
                      url="https://github.com/the-african-nightmare66"),
        ft.Text("📞  +264 81 305 2054", color="#374151"),
        ft.Text("📍  Ongwediva, Namibia", color="#374151"),
    )

    # ── FOOTER ────────────────────────────────────────────────────────────────
    footer = ft.Container(
        content=ft.Text(
            "© 2026 Wilhelm Wilson Shipandeni Moses | Personal Portfolio",
            text_align=ft.TextAlign.CENTER,
            color="#374151",
        ),
        padding=20,
    )

    # ── PAGE ──────────────────────────────────────────────────────────────────
    page.add(
        welcome,       divider(),
        header,        divider(),
        about,         divider(),
        skills,        divider(),
        stats,         divider(),
        quotewise,     divider(),
        matlab,        divider(),
        blog,          divider(),
        github,        divider(),
        reflection,    divider(),
        contact,       divider(),
        footer,
    )


ft.run(
    main,
    assets_dir="assets",
    view=ft.AppView.WEB_BROWSER,
    host="localhost",
    port=5000,
)
