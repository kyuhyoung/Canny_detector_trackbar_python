import cv2


m2_fn_m1_dir_p1_vid_p2_cam = 0
i_frm = -1
cap = None
im = None

def nothing():
    pass

def go_2_frame():
    if -1 == m2_fn_m1_dir_p1_vid_p2_cam:
        im = cv2.imread(li_path_img[i_frm], cv2.IMREAD_UNCHANGED)
    elif 1 == m2_fn_m1_dir_p1_vid_p2_cam:
        cap.set(2, i_frm)
        ret, im = cap.read()
        
        

def get_list_of_image_path_under_this_directory(dir_img, ext = ''):
    dir_img = os.path.expanduser(dir_img)
    li_fn_img = get_list_of_file_path_under_1st_with_2nd_extension(dir_img, ext)
    if is_this_empty_string(ext):
        li_fn_img = [fn for fn in li_fn_img if is_image_file(fn)]
    return sorted(li_fn_img)

def main(fn_or_dir_or_vid_or_cam):
    
    n_frm = 0
    m2_fn_m1_dir_p1_vid_p2_cam = 0
    if m2_fn_m1_dir_p1_vid_p2_cam > 0:
        cap = cv2.VideoCapture(fn_or_dir_or_vid_or_cam)
        if !cap.isOpened():        
            print('Can NOT open video or camera for : ', fn_or_dir_or_vid_or_cam)
            exit()
        print('width: {}, height : {}'.format(cap.get(3), cap.get(4)))
        if 1 == m2_fn_m1_dir_p1_vid_p2_cam:
            n_frm = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        im = cap.read()
    
    elif -1 == m2_fn_m1_dir_p1_vid_p2_cam:
        li_path_img = get_list_of_image_path_under_this_directory(fn_or_dir_or_vid_or_cam)
        n_frm = len(li_path_img):
        if 0 == n_frm:
            print('There is no image file under the directory : ', fn_or_dir_or_vid_or_cam)
            exit()
        im = cv2.imread(li_path_img[0], cv2.IMREAD_UNCHANGED)
    else:
        im = cv2.imread(fn_or_dir_or_vid_or_cam, cv2.IMREAD_UNCHANGED)


    cv2.namedWindow("Canny Edge")
    if n_frm:
        cv2.createTrackbar('# frame', 'Canny Edge', 0, n_frm, go_2_frame)
        cv2.setTrackbarPos('low threshold', 'Canny Edge', 0)
    cv2.createTrackbar('low threshold', 'Canny Edge', 0, 1000, nothing)
    cv2.createTrackbar('high threshold', 'Canny Edge', 0, 1000, nothing)

    cv2.setTrackbarPos('low threshold', 'Canny Edge', 50)
    cv2.setTrackbarPos('high threshold', 'Canny Edge', 150)

    cv2.imshow("Original", img_gray)

    while True:

        low = cv2.getTrackbarPos('low threshold', 'Canny Edge')
        high = cv2.getTrackbarPos('high threshold', 'Canny Edge')
        i_frm = cv2.getTrackbarPos('# frame', 'Canny Edge')

        img_canny = cv2.Canny(img_gray, low, high)
        cv2.imshow("Canny Edge", img_canny)

        if cv2.waitKey(1)&0xFF == 27:
            break


    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv[1])


