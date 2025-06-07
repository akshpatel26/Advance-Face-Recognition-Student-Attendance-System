from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import webbrowser
import os

class AboutDeveloper:
    def __init__(self, root):
        self.root = root
        self.root.title("About Developer - Aksh Patel")
        self.root.geometry("600x400")  
        self.root.minsize(1200, 700)     # reasonable minimum
        self.root.maxsize(1600, 900)    # up to 75% of screen
        
        # Center the window
        self.center_window()
        
        
        # Initialize photo variable
        self.photo = None
        
        # Create main scrollable frame
        self.create_scrollable_frame()
        
        # Create all sections
        self.create_header_section()
        self.create_main_content()
        self.create_skills_section()
        self.create_projects_section()
        self.create_footer()

    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"800x500+{x}+{y}")

    def create_scrollable_frame(self):
        """Create a scrollable main frame"""
        # Create canvas and scrollbar
        self.canvas = Canvas(self.root, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind mousewheel to canvas
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def create_header_section(self):
        """Create the header section with title and description"""
        header_frame = Frame(self.scrollable_frame, bg="white")
        header_frame.pack(pady=20, fill=X, padx=20)

        # Main title with gradient effect
        title_label = Label(
            header_frame, 
            text="About Developer", 
            font=("Segoe UI", 32, "bold"), 
            bg="white", 
            fg="#2c3e50"
        )
        title_label.pack()

        # Subtitle
        subtitle_label = Label(
            header_frame,
            text="Computer Engineering Student & Python Developer",
            font=("Segoe UI", 14, "italic"),
            bg="white",
            fg="#7f8c8d"
        )
        subtitle_label.pack(pady=(5, 15))

        # Description
        description_text = (
            "I'm a passionate Computer Engineering student with a strong interest in "
            "Python programming and Machine Learning. As a fresher, I've been "
            "actively learning and working on projects to build my understanding "
            "of core ML concepts, web development, and software engineering principles."
        )

        desc_label = Label(
            header_frame,
            text=description_text,
            font=("Segoe UI", 12),
            bg="white",
            fg="#34495e",
            wraplength=750,
            justify=CENTER,
        )
        desc_label.pack(pady=(0, 20))

    def create_main_content(self):
        """Create the main content with personal info and image"""
        content_frame = Frame(self.scrollable_frame, bg="white")
        content_frame.pack(padx=30, fill=BOTH, expand=True)

        # Left side - Personal Information
        info_frame = Frame(content_frame, bg="white")
        info_frame.grid(row=0, column=0, sticky="nw", padx=20, pady=10)

        # Professional title
        prof_title = Label(
            info_frame,
            text="Python Developer & ML Enthusiast",
            font=("Segoe UI", 20, "bold"),
            bg="white",
            fg="#2980b9",
        )
        prof_title.pack(anchor=W, pady=(0, 20))

        # Personal info in organized layout
        self.create_info_sections(info_frame)

        # Social media links
        self.create_social_links(info_frame)

        # Right side - Developer image with upload option
        self.create_image_section(content_frame)

    def create_info_sections(self, parent):
        """Create organized info sections"""
        # Personal Information Section
        personal_frame = LabelFrame(parent, text="Personal Information", 
                                  font=("Segoe UI", 12, "bold"), bg="white", 
                                  fg="#2c3e50", padx=10, pady=10)
        personal_frame.pack(fill=X, pady=(0, 15))

        info_grid = Frame(personal_frame, bg="white")
        info_grid.pack()

        # Left column
        left_col = Frame(info_grid, bg="white")
        left_col.grid(row=0, column=0, sticky="nw", padx=15)

        left_data = [
            ("📅 Birthday:", "26 Feb 2004"),
            ("📱 Phone:", "+91 9023942861"),
            ("🌍 Location:", "Gujarat, India"),
        ]

        for label, value in left_data:
            self.create_styled_info_row(left_col, label, value)

        # Right column
        right_col = Frame(info_grid, bg="white")
        right_col.grid(row=0, column=1, sticky="nw", padx=15)

        right_data = [
            ("🎂 Age:", "21"),
            ("🎓 Degree:", "Bachelor of Engineering"),
            ("📧 Email:", "akshpatel2602@gmail.com"),
        ]

        for label, value in right_data:
            self.create_styled_info_row(right_col, label, value)

    def create_styled_info_row(self, parent, label, value):
        """Create a styled info row"""
        frame = Frame(parent, bg="white")
        frame.pack(anchor=W, pady=8, fill=X)
        
        lbl = Label(frame, text=label, font=("Segoe UI", 11, "bold"), 
                   bg="white", fg="#34495e", width=12, anchor=W)
        lbl.pack(side=LEFT)
        
        val = Label(frame, text=value, font=("Segoe UI", 11), 
                   bg="white", fg="#7f8c8d")
        val.pack(side=LEFT, padx=(5, 0))

    def create_social_links(self, parent):
        """Create social media links section"""
        social_frame = LabelFrame(parent, text="Connect With Me", 
                                font=("Segoe UI", 12, "bold"), bg="white", 
                                fg="#2c3e50", padx=10, pady=10)
        social_frame.pack(fill=X, pady=(0, 15))

        button_frame = Frame(social_frame, bg="white")
        button_frame.pack()

        socials = [
            ("GitHub", "https://github.com/akshpatel26", "#333333", "💻"),
            ("WhatsApp", "https://wa.me/9023942861", "#25D366", "💬"),
            ("LinkedIn", "https://www.linkedin.com/in/aksh-patel-a1932a285/", "#0077B5", "💼"),
            ("Instagram", "https://www.instagram.com/aksh_patel_26/", "#E4405F", "📸"),
        ]

        for name, url, color, icon in socials:
            btn = Button(
                button_frame,
                text=f"{icon} {name}",
                font=("Segoe UI", 10, "bold"),
                bg=color,
                fg="white",
                relief=FLAT,
                cursor="hand2",
                padx=15,
                pady=8,
                command=lambda link=url: webbrowser.open_new(link),
            )
            btn.pack(side=LEFT, padx=5, pady=5)
            
            # Hover effects
            btn.bind("<Enter>", lambda e, b=btn, c=color: b.config(bg=self.darken_color(c)))
            btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(bg=c))

    def create_image_section(self, parent):
        """Create image section with upload functionality"""
        img_frame = Frame(parent, bg="white")
        img_frame.grid(row=0, column=1, sticky="ne", padx=20, pady=10)

        # Image container
        img_container = LabelFrame(img_frame, text="Developer Photo", 
                                 font=("Segoe UI", 12, "bold"), bg="white", 
                                 fg="#2c3e50", padx=15, pady=15)
        img_container.pack()

        # Try to load default image or show placeholder
        self.img_label = Label(img_container, bg="white")
        self.img_label.pack(pady=10)
        
        # Load image
        self.load_developer_image()

        # Upload button
        upload_btn = Button(
            img_container,
            text="📁 Change Photo",
            font=("Segoe UI", 10),
            bg="#3498db",
            fg="white",
            relief=FLAT,
            cursor="hand2",
            padx=15,
            pady=5,
            command=self.upload_image
        )
        upload_btn.pack(pady=(10, 0))

    def load_developer_image(self):
        """Load developer image or show placeholder"""
        try:
            # Try different possible paths
            possible_paths = [
                "images/contact.png",
                "contact.png",
                "../images/contact.png",
                "D:/Advance-Face-Recognition-Student-Attendance-System-Project/images/contact.png"
            ]
            
            image_loaded = False
            for path in possible_paths:
                if os.path.exists(path):
                    img = Image.open(path)
                    img = img.resize((200, 200), Image.Resampling.LANCZOS)
                    self.photo = ImageTk.PhotoImage(img)
                    self.img_label.config(image=self.photo)
                    image_loaded = True
                    break
            
            if not image_loaded:
                # Create placeholder
                self.create_placeholder_image()
                
        except Exception as e:
            self.create_placeholder_image()

    def create_placeholder_image(self):
        """Create a placeholder image"""
        placeholder_text = "👨‍💻\nDeveloper\nPhoto"
        self.img_label.config(
            text=placeholder_text,
            font=("Segoe UI", 16),
            fg="#bdc3c7",
            bg="#ecf0f1",
            width=15,
            height=8,
            relief=RIDGE,
            bd=2
        )

    def upload_image(self):
        """Allow user to upload a new image"""
        file_path = filedialog.askopenfilename(
            title="Select Developer Photo",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        
        if file_path:
            try:
                img = Image.open(file_path)
                img = img.resize((200, 200), Image.Resampling.LANCZOS)
                self.photo = ImageTk.PhotoImage(img)
                self.img_label.config(image=self.photo, text="")
                messagebox.showinfo("Success", "Image uploaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")

    def create_skills_section(self):
        """Create skills section"""
        skills_frame = LabelFrame(self.scrollable_frame, text="Technical Skills", 
                                font=("Segoe UI", 14, "bold"), bg="white", 
                                fg="#2c3e50", padx=20, pady=15)
        skills_frame.pack(fill=X, padx=30, pady=15)

        skills_data = [
            ("Programming Languages", ["Python", "C++", "SQL"]),
            ("Machine Learning", ["Scikit-learn", "Matplotlib", "Pandas", "NumPy","Seaborn"]),
            ("Tools & Technologies", ["Git", "VS Code", "Jupyter", "MySQL"])
        ]

        for category, skills in skills_data:
            cat_frame = Frame(skills_frame, bg="white")
            cat_frame.pack(fill=X, pady=8)
            
            cat_label = Label(cat_frame, text=f"{category}:", 
                            font=("Segoe UI", 11, "bold"), 
                            bg="white", fg="#2980b9")
            cat_label.pack(anchor=W)
            
            skills_text = " • ".join(skills)
            skills_label = Label(cat_frame, text=skills_text, 
                               font=("Segoe UI", 10), 
                               bg="white", fg="#7f8c8d")
            skills_label.pack(anchor=W, padx=20)

    def create_projects_section(self):
        """Create projects section"""
        projects_frame = LabelFrame(self.scrollable_frame, text="Featured Projects", 
                                  font=("Segoe UI", 14, "bold"), bg="white", 
                                  fg="#2c3e50", padx=20, pady=15)
        projects_frame.pack(fill=X, padx=30, pady=15)

        projects = [
            ("WhatsApp Chat Analyzer", "This application lets you analyze Whatsapp conversations in a very comprehensive manner, with charts, metrics and other forms of analysis."),
            ("Multiple Disease Prediction"," This project is Streamlit-based web app that predicts diseases  like Diabetes, Heart Disease, and Parkinson’s using ML models. It takes user input and provides instant results based on Real   healthcare datasets. "),
            ("Data Analysis Projects", "Various data science projects using Pandas and Matplotlib")
        ]

        for project, description in projects:
            proj_frame = Frame(projects_frame, bg="white")
            proj_frame.pack(fill=X, pady=8)
            
            proj_label = Label(proj_frame, text=f"🚀 {project}", 
                             font=("Segoe UI", 11, "bold"), 
                             bg="white", fg="#27ae60")
            proj_label.pack(anchor=W)
            
            desc_label = Label(proj_frame, text=description, 
                             font=("Segoe UI", 10), 
                             bg="white", fg="#7f8c8d")
            desc_label.pack(anchor=W, padx=20)

    def create_footer(self):
        """Create footer section"""
        footer_frame = Frame(self.scrollable_frame, bg="white")
        footer_frame.pack(fill=X, pady=20)

        footer_text = "© 2025 Aksh Patel | Computer Engineering Student | Python Developer"
        footer_label = Label(footer_frame, text=footer_text, 
                           font=("Segoe UI", 10, "italic"), 
                           bg="white", fg="#95a5a6")
        footer_label.pack()

    def darken_color(self, color):
        """Darken a hex color for hover effect"""
        # Simple color darkening - in a real app, you'd use a proper color library
        color_map = {
            "#333333": "#1a1a1a",
            "#25D366": "#1ea952",
            "#0077B5": "#005885",
            "#E4405F": "#d12954"
        }
        return color_map.get(color, color)


if __name__ == "__main__":
    root = Tk()
    app = AboutDeveloper(root)
    root.mainloop()