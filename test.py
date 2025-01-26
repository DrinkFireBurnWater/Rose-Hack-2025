import grabber
import model

balls = grabber.scrape_news('climate',('cnn','bbc'))
for i in range(5):
    print(balls[i])

balls2 = model.get_sentiments(balls)

print(balls2)