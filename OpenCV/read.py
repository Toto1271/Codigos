import cv2 as cv

int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv. INTER_AREA)




resized = resizeFrame(frame)
cv.imshow('Image', resized_image)
while True:
    isTrue,frame = capture.read()
    cv.imshow('VIDEO', frame)
    if cv.waitKey(1) & 0xFF==ord('d'):
     break
capture.release()
cv.destroyAllWindows

cv.waitKey(0)