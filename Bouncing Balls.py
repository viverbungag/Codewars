def bouncing_ball(h, bounce, window):
    # your code
    if h > 0 and bounce > 0 and bounce < 1 and window < h: 
        ans = 1
        h = h*bounce
        while h >= window:
            if h == window:
                break
            # bval = h*bounce
            else:
                print (h)
                h = h*bounce
                ans += 2
            
        return ans
    else:
        return -1


print (bouncing_ball(2, 0.5, 1))