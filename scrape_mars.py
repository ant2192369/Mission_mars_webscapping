{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import requests\n",
    "from selenium import webdriver\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {\"executable_path\":r\"C:\\Users\\Anthony\\.wdm\\chromedriver\\2.46\\win32\\chromedriver.exe\"}\n",
    "browser = Browser(\"chrome\", **executable_path, headless = False)\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mars InSight Lander's 'Mole' Pauses Digging\n",
      "After the mission's heat probe began hammering last week, it appears to have hit a rock. The team is analyzing data before they hammer again.\n"
     ]
    }
   ],
   "source": [
    "news_title = soup.find('div', class_='content_title').get_text()\n",
    "print(news_title)\n",
    "news_p = soup.find('div', class_='article_teaser_body').get_text()\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Image \n",
    "url_image = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit\"\n",
    "browser.visit(url_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/\n"
     ]
    }
   ],
   "source": [
    "#Getting the base url\n",
    "from urllib.parse import urlsplit\n",
    "base_url = \"{0.scheme}://{0.netloc}/\".format(urlsplit(url_image))\n",
    "print(base_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {\"executable_path\":r\"C:\\Users\\Anthony\\.wdm\\chromedriver\\2.46\\win32\\chromedriver.exe\"}\n",
    "browser = Browser(\"chrome\", **executable_path, headless = False)\n",
    "url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url)\n",
    "import time \n",
    "browser.click_link_by_partial_text('FULL IMAGE')\n",
    "time.sleep(3)\n",
    "browser.click_link_by_partial_text('more info')\n",
    "time.sleep(3)\n",
    "browser.click_link_by_partial_text('.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://photojournal.jpl.nasa.gov/jpeg/PIA19046.jpg\n"
     ]
    }
   ],
   "source": [
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')\n",
    "\n",
    "featured_img_url = soup.find('img').get('src')\n",
    "print(featured_img_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InSight sol 99 (2019-03-07) low -95.8ºC (-140.4ºF) high -13.3ºC (8.1ºF)\n",
      "winds from the SW at 4.2 m/s (9.5 mph) gusting to 12.0 m/s (26.8 mph)\n",
      "pressure at 7.20 hPapic.twitter.com/XRi0faFSv5\n"
     ]
    }
   ],
   "source": [
    "mars_weather_url = 'https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(mars_weather_url)\n",
    "time.sleep(1)\n",
    "mars_weather_html = browser.html\n",
    "mars_weather_soup = bs(mars_weather_html, 'html.parser')\n",
    "\n",
    "tweets = mars_weather_soup.find('ol', class_='stream-items')\n",
    "mars_weather = tweets.find('p', class_=\"tweet-text\").text\n",
    "print(mars_weather)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_facts = 'https://space-facts.com/mars/'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Values</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Parameter</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.52 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-153 to 20 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Values\n",
       "Parameter                                          \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.42 x 10^23 kg (10.7% Earth)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.52 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                  -153 to 20 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_mars_facts = table[0]\n",
    "df_mars_facts.columns = [\"Parameter\", \"Values\"]\n",
    "df_mars_facts.set_index([\"Parameter\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table border=\"1\" class=\"dataframe table table-striped\">\n",
      "  <thead>\n",
      "    <tr style=\"text-align: right;\">\n",
      "      <th></th>\n",
      "      <th></th>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Mars Planet Profile</th>\n",
      "      <th></th>\n",
      "    </tr>\n",
      "  </thead>\n",
      "  <tbody>\n",
      "    <tr>\n",
      "      <th>Equatorial Diameter:</th>\n",
      "      <td>6,792 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Polar Diameter:</th>\n",
      "      <td>6,752 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Mass:</th>\n",
      "      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Moons:</th>\n",
      "      <td>2 (Phobos &amp; Deimos)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Orbit Distance:</th>\n",
      "      <td>227,943,824 km (1.52 AU)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Orbit Period:</th>\n",
      "      <td>687 days (1.9 years)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Surface Temperature:</th>\n",
      "      <td>-153 to 20 °C</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>First Record:</th>\n",
      "      <td>2nd millennium BC</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>Recorded By:</th>\n",
      "      <td>Egyptian astronomers</td>\n",
      "    </tr>\n",
      "  </tbody>\n",
      "</table>\n"
     ]
    }
   ],
   "source": [
    "table = table_df.to_html(classes = 'table table-striped')\n",
    "print(table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "# hemispheres\n",
    "executable_path = {\"executable_path\":r\"C:\\Users\\Anthony\\.wdm\\chromedriver\\2.46\\win32\\chromedriver.exe\"}\n",
    "browser = Browser(\"chrome\", **executable_path, headless = False)\n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)\n",
    "\n",
    "html = browser.html\n",
    "soup = bs(html, 'html.parser')\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time \n",
    "hemispheres_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(hemispheres_url)\n",
    "html = browser.html\n",
    "soup = bs(html, \"html.parser\")\n",
    "mars_hemisphere = []\n",
    "\n",
    "products = soup.find(\"div\", class_ = \"result-list\" )\n",
    "hemispheres = products.find_all(\"div\", class_=\"item\")\n",
    "\n",
    "for hemisphere in hemispheres:\n",
    "    title = hemisphere.find(\"h3\").text\n",
    "    title = title.replace(\"Enhanced\", \"\")\n",
    "    end_link = hemisphere.find(\"a\")[\"href\"]\n",
    "    image_link = \"https://astrogeology.usgs.gov/\" + end_link    \n",
    "    browser.visit(image_link)\n",
    "    html = browser.html\n",
    "    soup=bs(html, \"html.parser\")\n",
    "    downloads = soup.find(\"div\", class_=\"downloads\")\n",
    "    image_url = downloads.find(\"a\")[\"href\"]\n",
    "    mars_hemisphere.append({\"title\": title, \"img_url\": image_url})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_hemisphere"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
