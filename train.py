from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import numpy as np
import os
from datetime import datetime
from time import strftime


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        def time():
            string =strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl=Label(title_lbl,font=("times new roman",14,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=130,height=60)
        time()      
                # Close button function
        def close_and_return():
            self.root.destroy()  # Close current window
        
        
        # Close button
        close_btn = Button(title_lbl, text="Close", font=("times new roman", 20, "bold"), bg="white", fg="Red", cursor="hand2", command=close_and_return)
        close_btn.place(x=1390, y=0, width=150, height=45) 
        

        img_top = Image.open("images/f1.png")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2",
                      command=self.train_classifier,
                      font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        img_bottom = Image.open("images/f2.png")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found!")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image_path in path:
            try:
                img = Image.open(image_path).convert('L')  # Convert to grayscale
                image_np = np.array(img, 'uint8')
                filename = os.path.split(image_path)[1]
                id = int(filename.split('.')[1])
                faces.append(image_np)
                ids.append(id)
                cv2.imshow("Training", image_np)
                cv2.waitKey(1)
            except Exception as e:
                print(f"Skipping {image_path}: {e}")

        ids = np.array(ids)

        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)

            output_dir = "classifier"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            clf.write(os.path.join(output_dir, "classifier.xml"))
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training Datasets Completed!")
        except Exception as e:
            messagebox.showerror("Error", f"Training failed: {e}")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
