{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "from tqdm import tqdm_notebook\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import seaborn as sns\n",
    "\n",
    "# matplot에서 한글폰트 깨짐현상 해결\n",
    "import platform\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib import font_manager, rc\n",
    "plt.rcParams['axes.unicode_minus'] = False\n",
    "\n",
    "path = 'c://Windows/Fonts/malgun.ttf'\n",
    "\n",
    "font_name = font_manager.FontProperties(fname=path).get_name()\n",
    "rc('font', family=font_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "통합데이터 = pd.read_csv(\"../data/통합데이터.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "통합데이터_피벗 = pd.pivot_table(통합데이터, index=[\"대여소명\",\"시\",\"거치대총개수\"], values=\"거치수량\")\n",
    "통합데이터_피벗.reset_index(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소명 = 통합데이터_피벗[\"대여소명\"].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 거치초과율 계산"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "거치초과율 = []\n",
    "거치초과량 = []\n",
    "거치이하량 = []\n",
    "거치대총개수 = []\n",
    "for i in 대여소명:\n",
    "    tmp = 통합데이터_피벗[통합데이터_피벗[\"대여소명\"] == i] \n",
    "    거치초과량_ = len(tmp[tmp[\"거치수량\"] > tmp[\"거치대총개수\"].iloc[0]])\n",
    "    거치이하량_ = len(tmp[tmp[\"거치수량\"] <= tmp[\"거치대총개수\"].iloc[0]])\n",
    "    \n",
    "    거치초과량.append(거치초과량_)\n",
    "    거치이하량.append(거치이하량_)\n",
    "    \n",
    "    거치대총개수.append(tmp[\"거치대총개수\"].iloc[0])\n",
    "    거치초과율.append(거치초과량_/(거치초과량_+거치이하량_))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성1 = pd.DataFrame({\"대여소명\":대여소명, \"거치초과율\":거치초과율,\"거치대총개수\":거치대총개수})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "tmp__ = pd.DataFrame({\"대여소명\":대여소명, \"거치초과율\":거치초과율,\"거치초과량\":거치초과량,\"거치이하량\":거치이하량,\"거치대총개수\":거치대총개수})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
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
       "      <th>대여소명</th>\n",
       "      <th>거치초과율</th>\n",
       "      <th>거치초과량</th>\n",
       "      <th>거치이하량</th>\n",
       "      <th>거치대총개수</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>강변역 4번출구 뒤</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>건국대학교 (입학정보관)</td>\n",
       "      <td>0.166667</td>\n",
       "      <td>4</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>건국대학교 (행정관)</td>\n",
       "      <td>0.208333</td>\n",
       "      <td>5</td>\n",
       "      <td>19</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>건국대학교 과학관(이과대) 앞</td>\n",
       "      <td>0.333333</td>\n",
       "      <td>8</td>\n",
       "      <td>16</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>건국대학교 학생회관</td>\n",
       "      <td>0.250000</td>\n",
       "      <td>6</td>\n",
       "      <td>18</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>광나루역 3번 출구</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>광남중학교</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>광양중학교 앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>광진경찰서</td>\n",
       "      <td>0.500000</td>\n",
       "      <td>12</td>\n",
       "      <td>12</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>광진광장 교통섬</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>광진구의회 앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>광진구청 앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>광진메디칼 앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>광진유진스웰</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>광진청소년수련관</td>\n",
       "      <td>0.583333</td>\n",
       "      <td>14</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>구의3동주민센터</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>구의공원(테크노마트 앞)</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>구의문주차장 앞</td>\n",
       "      <td>0.250000</td>\n",
       "      <td>6</td>\n",
       "      <td>18</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>구의삼성쉐르빌 앞</td>\n",
       "      <td>0.625000</td>\n",
       "      <td>15</td>\n",
       "      <td>9</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>구의아리수정수센터앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>국립정신 건강센터 앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>군자교교차로</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>군자역 7번출구 베스트샵 앞</td>\n",
       "      <td>0.500000</td>\n",
       "      <td>12</td>\n",
       "      <td>12</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>군자역2번출구</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>대림아크로리버 앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>더샵스타시티 C동 앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>뚝섬유원지역 1번출구 앞</td>\n",
       "      <td>0.041667</td>\n",
       "      <td>1</td>\n",
       "      <td>23</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>세종대학교</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>세종사이버대학교</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>신양초교앞 교차로</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>신자초교입구교차로</td>\n",
       "      <td>0.708333</td>\n",
       "      <td>17</td>\n",
       "      <td>7</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>아차산역 3번출구</td>\n",
       "      <td>0.458333</td>\n",
       "      <td>11</td>\n",
       "      <td>13</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>아차산역4번출구</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>어린이대공원역 3번출구 앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>어린이대공원역6번출구</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>어린이회관</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>영동대교 북단</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>용마사거리</td>\n",
       "      <td>0.416667</td>\n",
       "      <td>10</td>\n",
       "      <td>14</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>원일교회</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>자양나들목</td>\n",
       "      <td>0.375000</td>\n",
       "      <td>9</td>\n",
       "      <td>15</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>자양사거리 광진아크로텔 앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>자양중앙나들목</td>\n",
       "      <td>0.625000</td>\n",
       "      <td>15</td>\n",
       "      <td>9</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>잠실대교북단 교차로</td>\n",
       "      <td>0.291667</td>\n",
       "      <td>7</td>\n",
       "      <td>17</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43</th>\n",
       "      <td>중곡 성원APT 앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>중곡SK아파트앞</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>중곡역 1번출구</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>중앙농협 중곡지점</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>현대홈타운 뒷길</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>화양사거리</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                대여소명     거치초과율  거치초과량  거치이하량  거치대총개수\n",
       "0         강변역 4번출구 뒤  0.000000      0     24      19\n",
       "1      건국대학교 (입학정보관)  0.166667      4     20      10\n",
       "2        건국대학교 (행정관)  0.208333      5     19       5\n",
       "3   건국대학교 과학관(이과대) 앞  0.333333      8     16      10\n",
       "4         건국대학교 학생회관  0.250000      6     18      15\n",
       "5         광나루역 3번 출구  0.000000      0     24      10\n",
       "6              광남중학교  0.000000      0     24      20\n",
       "7            광양중학교 앞  0.000000      0     24      10\n",
       "8              광진경찰서  0.500000     12     12      10\n",
       "9           광진광장 교통섬  0.000000      0     24      20\n",
       "10           광진구의회 앞  0.000000      0     24      15\n",
       "11            광진구청 앞  0.000000      0     24      10\n",
       "12           광진메디칼 앞  0.000000      0     24      10\n",
       "13            광진유진스웰  0.000000      0     24      20\n",
       "14          광진청소년수련관  0.583333     14     10      10\n",
       "15          구의3동주민센터  0.000000      0     24      10\n",
       "16     구의공원(테크노마트 앞)  0.000000      0     24      20\n",
       "17          구의문주차장 앞  0.250000      6     18      10\n",
       "18         구의삼성쉐르빌 앞  0.625000     15      9      10\n",
       "19        구의아리수정수센터앞  0.000000      0     24      10\n",
       "20       국립정신 건강센터 앞  0.000000      0     24      20\n",
       "21            군자교교차로  0.000000      0     24      10\n",
       "22   군자역 7번출구 베스트샵 앞  0.500000     12     12       8\n",
       "23           군자역2번출구  0.000000      0     24      10\n",
       "24         대림아크로리버 앞  0.000000      0     24      10\n",
       "25       더샵스타시티 C동 앞  0.000000      0     24      15\n",
       "26     뚝섬유원지역 1번출구 앞  0.041667      1     23      15\n",
       "27             세종대학교  0.000000      0     24      15\n",
       "28          세종사이버대학교  0.000000      0     24      20\n",
       "29         신양초교앞 교차로  0.000000      0     24      12\n",
       "30         신자초교입구교차로  0.708333     17      7       5\n",
       "31         아차산역 3번출구  0.458333     11     13      10\n",
       "32          아차산역4번출구  0.000000      0     24      20\n",
       "33    어린이대공원역 3번출구 앞  0.000000      0     24      10\n",
       "34       어린이대공원역6번출구  0.000000      0     24      20\n",
       "35             어린이회관  0.000000      0     24      25\n",
       "36           영동대교 북단  0.000000      0     24      10\n",
       "37             용마사거리  0.416667     10     14      10\n",
       "38              원일교회  0.000000      0     24       8\n",
       "39             자양나들목  0.375000      9     15      20\n",
       "40    자양사거리 광진아크로텔 앞  0.000000      0     24      10\n",
       "41           자양중앙나들목  0.625000     15      9       5\n",
       "42        잠실대교북단 교차로  0.291667      7     17       8\n",
       "43        중곡 성원APT 앞  0.000000      0     24      10\n",
       "44          중곡SK아파트앞  0.000000      0     24      10\n",
       "45          중곡역 1번출구  0.000000      0     24      15\n",
       "46         중앙농협 중곡지점  0.000000      0     24      10\n",
       "47          현대홈타운 뒷길  0.000000      0     24      10\n",
       "48             화양사거리  0.000000      0     24      10"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tmp__"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Solution 적용"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "보정거치대개수 = []\n",
    "거치대총개수 = []\n",
    "\n",
    "for i in 대여소명:\n",
    "    tmp = 통합데이터[통합데이터[\"대여소명\"] == i]\n",
    "    tmp2 = pd.pivot_table(data=tmp, index=[\"시\"],values=\"거치수량\")-tmp[\"거치대총개수\"].iloc[0]\n",
    "    추가_거치대개수 = round(np.mean(tmp2[tmp2[\"거치수량\"]>=0])).iloc[0]\n",
    "\n",
    "    if math.isnan(추가_거치대개수) ==True:\n",
    "        추가_거치대개수=0\n",
    "    거치대총개수.append(tmp[\"거치대총개수\"].iloc[0])   \n",
    "    보정거치대개수.append(추가_거치대개수 + tmp[\"거치대총개수\"].iloc[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성2 = pd.DataFrame({\"대여소명\":대여소명,\"보정거치대개수\":보정거치대개수})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 보정 후 거치초과율 계산"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "통합데이터_피벗 = pd.merge(통합데이터_피벗, 대여소별특성2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "보정거치초과율 = []\n",
    "\n",
    "for i in 대여소명:\n",
    "    tmp = 통합데이터_피벗[통합데이터_피벗[\"대여소명\"] == i] \n",
    "    거치초과량 = len(tmp[tmp[\"거치수량\"] > tmp[\"보정거치대개수\"].iloc[0]])\n",
    "    거치이하량 = len(tmp[tmp[\"거치수량\"] <= tmp[\"보정거치대개수\"].iloc[0]])\n",
    "\n",
    "    보정거치초과율.append(거치초과량/(거치초과량+거치이하량))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성3 = pd.DataFrame({\"대여소명\":대여소명,\"보정거치초과율\":보정거치초과율})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 대여소별 상관계수"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "상관계수 = []\n",
    "for i in 대여소명:\n",
    "    tmp = 통합데이터[통합데이터[\"대여소명\"] == i]\n",
    "    tmp2 = np.corrcoef(tmp[\"반납수\"], tmp[\"대여수\"])[0,1]\n",
    "    상관계수.append(tmp2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성4 = pd.DataFrame({\"대여소명\":대여소명,\"상관계수\":상관계수})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "중곡지점 = 통합데이터[통합데이터[\"대여소명\"] == \"중앙농협 중곡지점\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 반납율 & 대여율"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "이용율 = pd.pivot_table(data=통합데이터, index=[\"대여소명\"], values=[\"반납수\",\"대여수\"], aggfunc=\"sum\")\n",
    "이용율.reset_index(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "이용율[\"반납율\"] = 이용율[\"반납수\"] / (이용율[\"반납수\"]+이용율[\"대여수\"])\n",
    "이용율[\"대여율\"] = 이용율[\"대여수\"] / (이용율[\"반납수\"]+이용율[\"대여수\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성5= 이용율[[\"대여소명\",\"반납율\",\"대여율\"]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 대여소별특성 1,2,3,4,5 병합"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성 = pd.merge(대여소별특성1, 대여소별특성2, on=\"대여소명\")\n",
    "대여소별특성 = pd.merge(대여소별특성, 대여소별특성3, on=\"대여소명\")\n",
    "대여소별특성 = pd.merge(대여소별특성, 대여소별특성4, on=\"대여소명\")\n",
    "대여소별특성 = pd.merge(대여소별특성, 대여소별특성5, on=\"대여소명\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성= 대여소별특성.sort_values(\"보정거치초과율\",ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 자전거 거치대수 이회차 보정(Solution 재활용)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "통합데이터 = pd.merge(통합데이터,대여소별특성2,on=\"대여소명\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "이회_보정거치대개수 = []\n",
    "\n",
    "for i in 대여소명:\n",
    "    tmp = 통합데이터[통합데이터[\"대여소명\"] == i]\n",
    "    tmp2 = pd.pivot_table(data=tmp, index=[\"시\"],values=\"거치수량\")-tmp[\"보정거치대개수\"].iloc[0]\n",
    "    추가_거치대개수 = round(np.mean(tmp2[tmp2[\"거치수량\"]>=0])).iloc[0]\n",
    "\n",
    "    if math.isnan(추가_거치대개수) ==True:\n",
    "        추가_거치대개수=0\n",
    "        \n",
    "    이회_보정거치대개수.append(추가_거치대개수 + tmp[\"보정거치대개수\"].iloc[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성6 = pd.DataFrame({\"대여소명\":대여소명,\"이회_보정거치대개수\":이회_보정거치대개수})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "통합데이터 = pd.merge(통합데이터,대여소별특성6, on=\"대여소명\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 이회보정 후 보정거치초과율(보정거치초과율 재활용)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "통합데이터_피벗 = pd.merge(통합데이터_피벗, 대여소별특성6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "이회_보정거치초과율 = []\n",
    "\n",
    "for i in 대여소명:\n",
    "    tmp = 통합데이터_피벗[통합데이터_피벗[\"대여소명\"] == i] \n",
    "    거치초과량 = len(tmp[tmp[\"거치수량\"] > tmp[\"이회_보정거치대개수\"].iloc[0]])\n",
    "    거치이하량 = len(tmp[tmp[\"거치수량\"] <= tmp[\"이회_보정거치대개수\"].iloc[0]])\n",
    "\n",
    "    이회_보정거치초과율.append(거치초과량/(거치초과량+거치이하량))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성7 = pd.DataFrame({\"대여소명\":대여소명,\"이회_보정거치초과율\":이회_보정거치초과율})"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 대여소별특성 병합"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성 = pd.merge(대여소별특성,대여소별특성7, on=\"대여소명\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성 = pd.merge(대여소별특성,대여소별특성6, on=\"대여소명\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성.sort_values(\"이회_보정거치초과율\",ascending=False, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
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
       "      <th>대여소명</th>\n",
       "      <th>거치초과율</th>\n",
       "      <th>거치대총개수</th>\n",
       "      <th>보정거치대개수</th>\n",
       "      <th>보정거치초과율</th>\n",
       "      <th>상관계수</th>\n",
       "      <th>반납율</th>\n",
       "      <th>대여율</th>\n",
       "      <th>이회_보정거치초과율</th>\n",
       "      <th>이회_보정거치대개수</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>자양중앙나들목</td>\n",
       "      <td>0.625</td>\n",
       "      <td>5</td>\n",
       "      <td>14.0</td>\n",
       "      <td>0.416667</td>\n",
       "      <td>0.006752</td>\n",
       "      <td>0.564378</td>\n",
       "      <td>0.435622</td>\n",
       "      <td>0.25</td>\n",
       "      <td>16.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      대여소명  거치초과율  거치대총개수  보정거치대개수   보정거치초과율      상관계수       반납율       대여율  \\\n",
       "2  자양중앙나들목  0.625       5     14.0  0.416667  0.006752  0.564378  0.435622   \n",
       "\n",
       "   이회_보정거치초과율  이회_보정거치대개수  \n",
       "2        0.25        16.0  "
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "대여소별특성.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "대여소별특성 = 대여소별특성[[\"대여소명\",\"거치대총개수\",\"보정거치대개수\",\"이회_보정거치대개수\",\\\n",
    "              \"거치초과율\",\"보정거치초과율\",\"이회_보정거치초과율\",\"상관계수\",\"반납율\",\"대여율\"]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## (실험)그래프표현"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 건국대학교 (행정관)\n",
    "행정관 = 통합데이터[통합데이터[\"대여소명\"] == \"건국대학교 (행정관)\"]\n",
    "y1= 행정관[\"거치대총개수\"].iloc[0]\n",
    "y2= 행정관[\"보정거치대개수\"].iloc[0]\n",
    "\n",
    "# 잠실대교북단 교차로\n",
    "교차로 = 통합데이터[통합데이터[\"대여소명\"] == \"잠실대교북단 교차로\"]\n",
    "y3= 교차로[\"보정거치대개수\"].iloc[0]\n",
    "y4= 교차로[\"이회_보정거치대개수\"].iloc[0]\n",
    "\n",
    "# 자양중앙나들목\n",
    "자양중앙나들목 = 통합데이터[통합데이터[\"대여소명\"] == \"자양중앙나들목\"]\n",
    "y5= 자양중앙나들목[\"거치대총개수\"].iloc[0]\n",
    "y6= 자양중앙나들목[\"보정거치대개수\"].iloc[0]\n",
    "y7= 자양중앙나들목[\"이회_보정거치대개수\"].iloc[0]\n",
    "\n",
    "# 건국대학교 (입학정보관)\n",
    "입학정보관 = 통합데이터[통합데이터[\"대여소명\"] == \"건국대학교 (입학정보관)\"]\n",
    "y8= 입학정보관[\"거치대총개수\"].iloc[0]\n",
    "y9= 입학정보관[\"이회_보정거치대개수\"].iloc[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1ce5024ef98>"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x576 with 4 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 다중그래프 그리기\n",
    "figure, ((ax1,ax2), (ax3,ax4)) = plt.subplots(nrows=2, ncols=2)\n",
    "\n",
    "figure.set_size_inches(10, 8)\n",
    "\n",
    "# 건국대학교 (행정관)\n",
    "ax1.axhline(y=y1,color=\"black\")\n",
    "ax1.axhline(y=6,color=\"red\")\n",
    "sns.barplot(data=행정관, x=\"시\", y=\"거치수량\",ax=ax1)\n",
    "\n",
    "# 잠실대교북단 교차로\n",
    "ax2.axhline(y=y3,color=\"black\")\n",
    "ax2.axhline(y=y4,color=\"red\")\n",
    "sns.barplot(data=교차로, x=\"시\", y=\"거치수량\",ax=ax2)\n",
    "\n",
    "# 자양중앙나들목\n",
    "ax3.axhline(y=y5,color=\"black\")\n",
    "ax3.axhline(y=y6,color=\"blue\")\n",
    "ax3.axhline(y=y7,color=\"red\")\n",
    "sns.barplot(data=자양중앙나들목, x=\"시\", y=\"거치수량\",ax=ax3)\n",
    "\n",
    "# 입학정보관\n",
    "ax4.axhline(y=y8,color=\"black\")\n",
    "ax4.axhline(y=y9,color=\"red\")\n",
    "sns.barplot(data=입학정보관, x=\"시\", y=\"거치수량\",ax=ax4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
