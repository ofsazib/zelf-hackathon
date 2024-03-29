# Zelf Hackathon

The goal is to create a simple Django backend where users can manage restaurants and menus.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ofsazib/zelf-hackathon.git
    ```

2. Navigate to the project directory:

    ```bash
    cd zelf-hackathon
    ```

3. Create a virtual environment and activate it

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Add `.env` file for environment variables:

    ```
    ZELF_HACK_API_KEY=
    ZELF_HACK_API_BASE_URL=https://hackapi.hellozelf.com
    ```

6. Apply migrations:

    ```bash
    python manage.py makemigrations && python manage.py migrate
    ```

## Usage

Describe how to use your Django app. Include any necessary steps, configurations, or prerequisites.

```bash
python projectile/manage.py runserver
python projectile/manage.py createsuperuser
```
## API

### Content List APi with author details
The API currently have no authentication

```
http://localhost:8000/api/v1/core/contents/?page=1
```
### Sample API response
```json
    {
    "page": 1,
    "next": 2,
    "data": [
        {
            "unique_id": 1996096,
            "unique_uuid": "31fca27a-9d67-458d-8e60-5be49a7933db",
            "origin_unique_id": "CqiKhfMA0iu",
            "creation_info": {
                "created_at": "2023-05-12T13:41:53.019333Z",
                "timestamp": "2023-05-12T13:41:53.019333Z"
            },
            "author": {
                "id": 919301,
                "username": "stuffedddd"
            },
            "context": {
                "main_text": "@pizzahuteg",
                "token_count": 1,
                "char_count": 11,
                "tag_count": 1
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/CqiKhfMA0iu"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/2686819e-aac6-434c-83db-ab02b541699c.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2992,
                        "count": 119778
                    },
                    "views": {
                        "id": 2885,
                        "count": 2600000
                    },
                    "comments": {
                        "id": 2293,
                        "count": 199
                    }
                }
            },
            "author_details": {
                "unique_id": 919301,
                "unique_uuid": "ig_stuffedddd",
                "origin_unique_id": "ig_stuffedddd",
                "info": {
                    "name": "Ayad Ayad | Food Blogger",
                    "platform": "instagram"
                },
                "username": "stuffedddd",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 5721,
                            "count": "89100"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://nyc3.digitaloceanspaces.com/hellozelf/content/b0465689-8fd7-4845-8c3c-9752e0811643.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "🍔 | Food Blogger 📸👨🏼‍⚖️ | Honest food ratings ⭐️📍 | Cairo, Egypt 🇪🇬📩 | DM for collabs 😍"
                }
            }
        },
        {
            "unique_id": 2571489,
            "unique_uuid": "8303de7d-eb22-4984-9964-4fd7c1d99259",
            "origin_unique_id": "7229439285236108586",
            "creation_info": {
                "created_at": "2023-05-04T21:16:55Z",
                "timestamp": "2023-05-04T21:16:55Z"
            },
            "author": {
                "id": 302048,
                "username": "sephora"
            },
            "context": {
                "main_text": "#SephoraSquad member @ADAN out here finding the perfect shade of @makeupbymario Surreal Skin Foundation using Color iQ.",
                "token_count": 17,
                "char_count": 119,
                "tag_count": 2
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@sephora/video/7229439285236108586"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/001c4eff-5af7-4fa3-9daa-9f6631ebbe96.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2535,
                        "count": 15300
                    },
                    "views": {
                        "id": 2604,
                        "count": 12100000
                    },
                    "comments": {
                        "id": 2821,
                        "count": 59
                    }
                }
            },
            "author_details": {
                "unique_id": 302048,
                "unique_uuid": "279484737629323264",
                "origin_unique_id": "279484737629323264",
                "info": {
                    "name": "sephora",
                    "platform": "instagram"
                },
                "username": "sephora",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 7402,
                            "count": "931900"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://p16-sign-sg.tiktokcdn.com/aweme/1080x1080/tos-alisg-avt-0068/smg71630d66b7a573be2525c01e74f615fe.jpeg?x-expires=1678014000&x-signature=v0NHfB5gs46Cuhx4I1A0QOHdmjA%3D"
                    ]
                },
                "texts": {
                    "profile_text": "We belong to something beautiful."
                }
            }
        },
        {
            "unique_id": 2390098,
            "unique_uuid": "8effbdaf-03c7-4679-b31c-4e733fbaa544",
            "origin_unique_id": "Cs878esgRSN",
            "creation_info": {
                "created_at": "2023-05-29T00:00:00Z",
                "timestamp": "2023-05-29T00:00:00Z"
            },
            "author": {
                "id": 1056801,
                "username": "sesamestreet"
            },
            "context": {
                "main_text": "Everyone is always welcome on Sesame Street. Let’s celebrate LGBTQIA+ people in our communities this Pride and every day! Happy #PrideMonth! 🏳️‍🌈",
                "token_count": 22,
                "char_count": 145,
                "tag_count": 2
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/Cs878esgRSN"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/2baed931-6b96-4a37-be47-fa7e34d37f91.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2994,
                        "count": 136540
                    },
                    "views": {
                        "id": 2224,
                        "count": 1600000
                    },
                    "comments": {
                        "id": 2852,
                        "count": 3352
                    }
                }
            },
            "author_details": {
                "unique_id": 1056801,
                "unique_uuid": "ig_sesamestreet",
                "origin_unique_id": "ig_sesamestreet",
                "info": {
                    "name": "sesamestreet",
                    "platform": "instagram"
                },
                "username": "sesamestreet",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 1662,
                            "count": "877000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        ""
                    ]
                },
                "texts": {
                    "profile_text": "sesamestreet"
                }
            }
        },
        {
            "unique_id": 4250292,
            "unique_uuid": "df7f2907-3e3e-46d1-89ab-565073a92a7e",
            "origin_unique_id": "7187503502539705642",
            "creation_info": {
                "created_at": "2023-01-11T21:04:41Z",
                "timestamp": "2023-01-11T21:04:41Z"
            },
            "author": {
                "id": 301482,
                "username": "mirandaalol"
            },
            "context": {
                "main_text": "Life-proof ur hair anywhere using @Living Proof, Inc.  Perfect Hair Day Dry Shampoo ✨ sold at @sephora & @Ulta Beauty  #livingproofinc #livingmyproof ",
                "token_count": 25,
                "char_count": 150,
                "tag_count": 3
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@mirandaalol/video/7187503502539705642"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/aa2bdb1f-34ff-4c63-8966-e005a04fd23e.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2675,
                        "count": 436700
                    },
                    "views": {
                        "id": 2444,
                        "count": 17300000
                    },
                    "comments": {
                        "id": 3150,
                        "count": 915
                    }
                }
            },
            "author_details": {
                "unique_id": 301482,
                "unique_uuid": "18267432",
                "origin_unique_id": "18267432",
                "info": {
                    "name": "miranda rae",
                    "platform": "instagram"
                },
                "username": "mirandaalol",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 7723,
                            "count": "7700000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://hellozelf.nyc3.cdn.digitaloceanspaces.com/content/26a1a30e-86b0-4d43-927d-653aefdbb200.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "yes I change my hair color a lot, I have issues 🤘🏽\nbiz : miranda@project15.co"
                }
            }
        },
        {
            "unique_id": 4811307,
            "unique_uuid": "caffd0ef-a34f-4a5b-8f96-ee0fad62e1dd",
            "origin_unique_id": "CwA290FOGga",
            "creation_info": {
                "created_at": "2023-08-16T00:00:00Z",
                "timestamp": "2023-08-16T00:00:00Z"
            },
            "author": {
                "id": 1774416,
                "username": "crocs"
            },
            "context": {
                "main_text": "The next best thing to tractor tippin’. Lightning McQueen is back! Link in bio.​",
                "token_count": 14,
                "char_count": 80,
                "tag_count": 1
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/CwA290FOGga"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/eae99d88-b121-46b3-a9fb-4935dc4b1395.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2286,
                        "count": 1300000
                    },
                    "views": {
                        "id": 2708,
                        "count": 18200000
                    },
                    "comments": {
                        "id": 2415,
                        "count": 12
                    }
                }
            },
            "author_details": {
                "unique_id": 1774416,
                "unique_uuid": "ig_crocs",
                "origin_unique_id": "ig_crocs",
                "info": {
                    "name": "Crocs Shoes",
                    "platform": "instagram"
                },
                "username": "crocs",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 3027,
                            "count": "2000000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://nyc3.digitaloceanspaces.com/hellozelf/content/f0048bb8-8c4c-41f5-ad78-4a7b7ea0d18f.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "Follow if you’re a real fan\ncrocs.shoes/ShrekXCrocs"
                }
            }
        },
        {
            "unique_id": 396032,
            "unique_uuid": "327e76de-125b-4e4a-b0a1-28af1a94eb0a",
            "origin_unique_id": "7185940813895961899",
            "creation_info": {
                "created_at": "2023-01-07T16:00:43Z",
                "timestamp": "2023-01-07T16:00:43Z"
            },
            "author": {
                "id": 301643,
                "username": "allierosss"
            },
            "context": {
                "main_text": "My man has no idea how much makeup costs 😅 #sephorahaul #sephora #sephorahaul #makeuphaul #shoppinghaul ",
                "token_count": 16,
                "char_count": 104,
                "tag_count": 6
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@allierosss/video/7185940813895961899"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/b5e0e7ea-f901-4997-bb17-945230edb015.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 3005,
                        "count": 1400000
                    },
                    "views": {
                        "id": 2903,
                        "count": 11200000
                    },
                    "comments": {
                        "id": 2379,
                        "count": 2668
                    }
                }
            },
            "author_details": {
                "unique_id": 301643,
                "unique_uuid": "6781986373924258822",
                "origin_unique_id": "6781986373924258822",
                "info": {
                    "name": "Allie | Beauty & stuff",
                    "platform": "instagram"
                },
                "username": "allierosss",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 9039,
                            "count": "253700"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://hellozelf.nyc3.cdn.digitaloceanspaces.com/content/846b8f75-90a7-4bef-8201-5e45a3e7d238.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "boston \ninsta _allieross_\nYouTube allierosss\n\n💌 arosscollaborations@gmail.com"
                }
            }
        },
        {
            "unique_id": 4811313,
            "unique_uuid": "f2485aea-9053-4372-8a61-37beb214cc8d",
            "origin_unique_id": "CxGQN8pMpSY",
            "creation_info": {
                "created_at": "2023-09-13T00:00:00Z",
                "timestamp": "2023-09-13T00:00:00Z"
            },
            "author": {
                "id": 1774416,
                "username": "crocs"
            },
            "context": {
                "main_text": "WHAT ARE YOU DOING IN MY SWAMP??? Run, don’t walk to crocs.com!",
                "token_count": 12,
                "char_count": 63,
                "tag_count": 1
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/CxGQN8pMpSY"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/f3146925-6bd6-41bd-aa47-5ffb2ec45e18.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2428,
                        "count": 316000
                    },
                    "views": {
                        "id": 2845,
                        "count": 4100000
                    },
                    "comments": {
                        "id": 2393,
                        "count": 2300
                    }
                }
            },
            "author_details": {
                "unique_id": 1774416,
                "unique_uuid": "ig_crocs",
                "origin_unique_id": "ig_crocs",
                "info": {
                    "name": "Crocs Shoes",
                    "platform": "instagram"
                },
                "username": "crocs",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 3027,
                            "count": "2000000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://nyc3.digitaloceanspaces.com/hellozelf/content/f0048bb8-8c4c-41f5-ad78-4a7b7ea0d18f.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "Follow if you’re a real fan\ncrocs.shoes/ShrekXCrocs"
                }
            }
        },
        {
            "unique_id": 533601,
            "unique_uuid": "0632ce2c-174a-4d2c-8fcd-cfaa8d522ccc",
            "origin_unique_id": "7197091208563428654",
            "creation_info": {
                "created_at": "2023-02-06T17:09:50Z",
                "timestamp": "2023-02-06T17:09:50Z"
            },
            "author": {
                "id": 363621,
                "username": "fentybeauty"
            },
            "context": {
                "main_text": "That #FENTYGAMEFACE never fumbles! 💯🏈 Start the play with a layer of #HYDRAVIZOR to tackle any SPF worries 🌞 Then, touchdown on #PROFILTRFOUNDATION for that fresh AF, soft matte flex 💪🏿💪🏾💪🏽 #GAMEDAY is just 6 days away, so re-up on the essentials now to prep for the big day at the 🔗 in bio, @sephora, @sephoracanada, and #sephoraxkohls 🏆",
                "token_count": 49,
                "char_count": 338,
                "tag_count": 6
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@fentybeauty/video/7197091208563428654"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/2438ac58-dbfd-4e5b-bd22-bf4e9af1d41f.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2345,
                        "count": 2200000
                    },
                    "views": {
                        "id": 3125,
                        "count": 18000000
                    },
                    "comments": {
                        "id": 3182,
                        "count": 3881
                    }
                }
            },
            "author_details": {
                "unique_id": 363621,
                "unique_uuid": "218606766895595520",
                "origin_unique_id": "218606766895595520",
                "info": {
                    "name": "Fenty Beauty",
                    "platform": "instagram"
                },
                "username": "fentybeauty",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 8940,
                            "count": "2600000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://p16-sign-sg.tiktokcdn.com/aweme/1080x1080/tos-alisg-avt-0068/smg8cbf53211e80271123ad300a11e337a7.jpeg?x-expires=1678039200&x-signature=jX1US7OnAIR1JincNsKgv%2Fjgr38%3D"
                    ]
                },
                "texts": {
                    "profile_text": "Fenty Beauty by RIHANNA ✨\n#CrueltyFree 🖤\nShop the looks! 👀 ⬇️"
                }
            }
        },
        {
            "unique_id": 4811328,
            "unique_uuid": "f926f47f-954f-421b-aad8-26b31631e812",
            "origin_unique_id": "Cv-X1_KA1fp",
            "creation_info": {
                "created_at": "2023-08-16T00:00:00Z",
                "timestamp": "2023-08-16T00:00:00Z"
            },
            "author": {
                "id": 1774416,
                "username": "crocs"
            },
            "context": {
                "main_text": "KA-CHOW! It’s happening tomorrow! Available on Crocs.com 8/16 for EQL early access. Available 8/17 at Crocs retail and select partners.",
                "token_count": 20,
                "char_count": 135,
                "tag_count": 1
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/Cv-X1_KA1fp"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/2ef30b79-7760-4e37-bdd1-a08b25615de0.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 3050,
                        "count": 133000
                    },
                    "views": {
                        "id": 2856,
                        "count": 1800000
                    },
                    "comments": {
                        "id": 3064,
                        "count": 1739
                    }
                }
            },
            "author_details": {
                "unique_id": 1774416,
                "unique_uuid": "ig_crocs",
                "origin_unique_id": "ig_crocs",
                "info": {
                    "name": "Crocs Shoes",
                    "platform": "instagram"
                },
                "username": "crocs",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 3027,
                            "count": "2000000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://nyc3.digitaloceanspaces.com/hellozelf/content/f0048bb8-8c4c-41f5-ad78-4a7b7ea0d18f.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "Follow if you’re a real fan\ncrocs.shoes/ShrekXCrocs"
                }
            }
        },
        {
            "unique_id": 5269185,
            "unique_uuid": "b904a9e3-67a8-4859-b8ac-7d4d2110dc80",
            "origin_unique_id": "7269860236641586474",
            "creation_info": {
                "created_at": "2023-08-21T19:30:57Z",
                "timestamp": "2023-08-21T19:30:57Z"
            },
            "author": {
                "id": 44508,
                "username": "pamelapedrozaa"
            },
            "context": {
                "main_text": "Replying to @Billy 🇬🇧🇮🇪✝️ ♾️ ✈️ #cotton #pad #sephora #bacteria ",
                "token_count": 11,
                "char_count": 64,
                "tag_count": 5
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@pamelapedrozaa/video/7269860236641586474"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/4ebf1a55-2cb1-4679-b732-07d68229c706.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2431,
                        "count": 500500
                    },
                    "views": {
                        "id": 3111,
                        "count": 12600000
                    },
                    "comments": {
                        "id": 2216,
                        "count": 598
                    }
                }
            },
            "author_details": {
                "unique_id": 44508,
                "unique_uuid": "6779687848977351685",
                "origin_unique_id": "6779687848977351685",
                "info": {
                    "name": "pamelapedrozaa",
                    "platform": "instagram"
                },
                "username": "pamelapedrozaa",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 3644,
                            "count": "1300000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://p16-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/5ae514bdc88d81460484d1d50f24f4eb~c5_1080x1080.jpeg?x-expires=1678014000&x-signature=n9CruNZmhLLsxsgQzCA6tKIXNuM%3D"
                    ]
                },
                "texts": {
                    "profile_text": "Always be yourself ✨\n\n✨Pammakeup28@gmail.com"
                }
            }
        },
        {
            "unique_id": 3577104,
            "unique_uuid": "0e1a92a7-e8a0-41ef-acd3-facb3fc805e0",
            "origin_unique_id": "Crdw5UstZ0M",
            "creation_info": {
                "created_at": "2023-04-25T00:00:00Z",
                "timestamp": "2023-04-25T00:00:00Z"
            },
            "author": {
                "id": 1378449,
                "username": "liquiddeath"
            },
            "context": {
                "main_text": "Turn your dreams into reality with the @liquiddeath x @travisbarker Enema of the State Collectible Enema Kit.",
                "token_count": 17,
                "char_count": 109,
                "tag_count": 1
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/Crdw5UstZ0M"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/c9d78909-1188-486d-b966-9bd26feb2a30.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2864,
                        "count": 283844
                    },
                    "views": {
                        "id": 3162,
                        "count": 6700000
                    },
                    "comments": {
                        "id": 2496,
                        "count": 6826
                    }
                }
            },
            "author_details": {
                "unique_id": 1378449,
                "unique_uuid": "ig_liquiddeath",
                "origin_unique_id": "ig_liquiddeath",
                "info": {
                    "name": "Liquid Death",
                    "platform": "instagram"
                },
                "username": "liquiddeath",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 3531,
                            "count": "2300000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://nyc3.digitaloceanspaces.com/hellozelf/content/7b642903-1ab2-48de-a8d0-280d8cb07d92.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "Don’t be scared. It’s just water & iced tea.#MurderYourThirst #DeathToPlastic ⁣♻️\nlinktr.ee/liquiddeath"
                }
            }
        },
        {
            "unique_id": 4841051,
            "unique_uuid": "d633c858-cfd9-404b-914d-e3ca56ffa5d4",
            "origin_unique_id": "7066991947482828079",
            "creation_info": {
                "created_at": "2022-02-21T02:58:04Z",
                "timestamp": "2022-02-21T02:58:04Z"
            },
            "author": {
                "id": 154235,
                "username": "bestbuytok6"
            },
            "context": {
                "main_text": "#SephoraLipLooks do you know what is it? #cosmetics #makeup #beauty #eyebrowpencil #fyp",
                "token_count": 12,
                "char_count": 87,
                "tag_count": 7
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@bestbuytok6/video/7066991947482828079"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/6fddc7ee-3c09-454f-879b-329eff456334.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2198,
                        "count": 136900
                    },
                    "views": {
                        "id": 2432,
                        "count": 12800000
                    },
                    "comments": {
                        "id": 2645,
                        "count": 151
                    }
                }
            },
            "author_details": {
                "unique_id": 154235,
                "unique_uuid": "7039911421694559237",
                "origin_unique_id": "7039911421694559237",
                "info": {
                    "name": "Bestbuytok6",
                    "platform": "instagram"
                },
                "username": "bestbuytok6",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 1888,
                            "count": "173600"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://nyc3.digitaloceanspaces.com/hellozelf/content/caaa589b-a680-4b8a-9a21-257a22bd74d7.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "Big discount in keychains & cosmetics\nFree shipping, buy in\nbestbuytok.com"
                }
            }
        },
        {
            "unique_id": 3577092,
            "unique_uuid": "499eb12f-3a35-4c62-a423-cfafe71bd210",
            "origin_unique_id": "Cp5dUxYp13o",
            "creation_info": {
                "created_at": "2023-03-17T00:00:00Z",
                "timestamp": "2023-03-17T00:00:00Z"
            },
            "author": {
                "id": 1378449,
                "username": "liquiddeath"
            },
            "context": {
                "main_text": "The only healthy beverage suitable for St. Paddy’s Day.",
                "token_count": 9,
                "char_count": 55,
                "tag_count": 1
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/Cp5dUxYp13o"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/388222b9-a8f3-4142-8d5b-ac5d97a12946.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2442,
                        "count": 101770
                    },
                    "views": {
                        "id": 2982,
                        "count": 2300000
                    },
                    "comments": {
                        "id": 2666,
                        "count": 469
                    }
                }
            },
            "author_details": {
                "unique_id": 1378449,
                "unique_uuid": "ig_liquiddeath",
                "origin_unique_id": "ig_liquiddeath",
                "info": {
                    "name": "Liquid Death",
                    "platform": "instagram"
                },
                "username": "liquiddeath",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 3531,
                            "count": "2300000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://nyc3.digitaloceanspaces.com/hellozelf/content/7b642903-1ab2-48de-a8d0-280d8cb07d92.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "Don’t be scared. It’s just water & iced tea.#MurderYourThirst #DeathToPlastic ⁣♻️\nlinktr.ee/liquiddeath"
                }
            }
        },
        {
            "unique_id": 395920,
            "unique_uuid": "f964866a-195e-4611-81f0-ed3539389521",
            "origin_unique_id": "6947846782365764869",
            "creation_info": {
                "created_at": "2021-04-06T01:14:03Z",
                "timestamp": "2021-04-06T01:14:03Z"
            },
            "author": {
                "id": 302876,
                "username": "anxietycouple"
            },
            "context": {
                "main_text": "It actually worked!!!! #foryou #fyp #sephora #ulta #makeup #shoppingspree #relatable",
                "token_count": 10,
                "char_count": 84,
                "tag_count": 8
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@anxietycouple/video/6947846782365764869"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/d772542c-a30a-4a20-9f73-c942fd0a8f50.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2569,
                        "count": 1700000
                    },
                    "views": {
                        "id": 2539,
                        "count": 11200000
                    },
                    "comments": {
                        "id": 2433,
                        "count": 0
                    }
                }
            },
            "author_details": {
                "unique_id": 302876,
                "unique_uuid": "6741591536436511749",
                "origin_unique_id": "6741591536436511749",
                "info": {
                    "name": "Anxietycouple",
                    "platform": "instagram"
                },
                "username": "anxietycouple",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 9347,
                            "count": "13600000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://hellozelf-dev.nyc3.cdn.digitaloceanspaces.com/content/a86519a4-ea16-4116-8d3b-993e8d0b6744.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "Love you all💚\n📧anxietycouple1@gmail.com\nCoupert app👇🏻👇🏻"
                }
            }
        },
        {
            "unique_id": 4630010,
            "unique_uuid": "a698c3fc-2bb3-4ae8-bfa3-7a3e93325751",
            "origin_unique_id": "CtiNC-SAoc_",
            "creation_info": {
                "created_at": "2023-06-16T00:00:00Z",
                "timestamp": "2023-06-16T00:00:00Z"
            },
            "author": {
                "id": 1712274,
                "username": "nandmahasuwan"
            },
            "context": {
                "main_text": "Did someone say water? 👀•Fest tix and rave gear are in the 🔗’s in my biiio. I appreciate any and all support from y’all. 🫶@moonrisefest @hardfest @nocturnalwland @escapehalloween @edc_orlando Fit by @clutchloop @genzoutdoor Code Nand to save $!•#ravedad #ravers #ravingaddict #raves #ravelife #edmlifestyle #ravebabe #ravebaby #festivalvibes #ravehumor #edmhumor #festivalhumor #plurnation #plurvibes #ravegirl #ravedaddy #raving",
                "token_count": 54,
                "char_count": 429,
                "tag_count": 18
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/CtiNC-SAoc_"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/68eaf386-ca9e-42fd-925a-8f150bfe0df6.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2546,
                        "count": 206000
                    },
                    "views": {
                        "id": 2792,
                        "count": 4400000
                    },
                    "comments": {
                        "id": 3087,
                        "count": 453
                    }
                }
            },
            "author_details": {
                "unique_id": 1712274,
                "unique_uuid": "ig_nandmahasuwan",
                "origin_unique_id": "ig_nandmahasuwan",
                "info": {
                    "name": "Nand - Your Rave Dad!",
                    "platform": "instagram"
                },
                "username": "nandmahasuwan",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 1986,
                            "count": "25200"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://nyc3.digitaloceanspaces.com/hellozelf/content/40d541f2-2dfa-4be2-91fe-15c2b13206a7.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "It's me Your Rave Dad! Aggressively asking you to drink water 😊Festival • @impeakingpod Host • Lifestyle My ESSENTIALS- @clutchloop - @genzoutdoor\n"
                }
            }
        },
        {
            "unique_id": 5436412,
            "unique_uuid": "9e0dff56-2264-4afd-bbc5-72b740d08496",
            "origin_unique_id": "7293259898354158854",
            "creation_info": {
                "created_at": "2023-10-23T20:53:20Z",
                "timestamp": "2023-10-23T20:53:20Z"
            },
            "author": {
                "id": 979810,
                "username": "katiefanggg"
            },
            "context": {
                "main_text": "My all time favorite @Saie products to snag at the @sephora sale!! 🛍️ #saiepartner #saiebeauty #sephorasale #sephorasalepicks",
                "token_count": 17,
                "char_count": 125,
                "tag_count": 5
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@katiefanggg/video/7293259898354158854"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/e9b1bc38-19ac-42ea-b5ef-2da7b10b30ac.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 3051,
                        "count": 266500
                    },
                    "views": {
                        "id": 2998,
                        "count": 10100000
                    },
                    "comments": {
                        "id": 2954,
                        "count": 606
                    }
                }
            },
            "author_details": {
                "unique_id": 979810,
                "unique_uuid": "6919594516106331141",
                "origin_unique_id": "6919594516106331141",
                "info": {
                    "name": "Katie Fang",
                    "platform": "instagram"
                },
                "username": "katiefanggg",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 6474,
                            "count": "4000000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://nyc3.digitaloceanspaces.com/hellozelf/content/88c6c0fb-b5a9-4e45-b9e7-fe6aa158a91e.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "💌KatieFangTeam@unitedtalent.com\n\nhttps://shopmy.us/katiefang"
                }
            }
        },
        {
            "unique_id": 2028846,
            "unique_uuid": "1b2fb3a0-2fa1-4e22-9e13-daf6667f4165",
            "origin_unique_id": "CrqGiMPsJxo",
            "creation_info": {
                "created_at": "2023-04-30T00:00:00Z",
                "timestamp": "2023-04-30T00:00:00Z"
            },
            "author": {
                "id": 934041,
                "username": "maybelline"
            },
            "context": {
                "main_text": "Wow! Can you believe Lia pranked Chaeryeong with our #tattooliner 🤣 She thought she had a tattoo when it was actually our #tattooliner!!! @itzy.all.in.us #TATTOOLINERCHALLENGE",
                "token_count": 25,
                "char_count": 175,
                "tag_count": 4
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/CrqGiMPsJxo"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/0364fe3b-ed0c-44fc-8424-de592f1d6cee.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2906,
                        "count": 423420
                    },
                    "views": {
                        "id": 2760,
                        "count": 3400000
                    },
                    "comments": {
                        "id": 2942,
                        "count": 827
                    }
                }
            },
            "author_details": {
                "unique_id": 934041,
                "unique_uuid": "ig_maybelline",
                "origin_unique_id": "ig_maybelline",
                "info": {
                    "name": "Maybelline New York",
                    "platform": "instagram"
                },
                "username": "maybelline",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 6721,
                            "count": "11700000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        ""
                    ]
                },
                "texts": {
                    "profile_text": "💄Maybe it’s Maybelline💋📍Born in New York🚕🗽🔗 Learn about our mental health initiative Brave Together ⬇️ www.maybelline.com/bravetogether"
                }
            }
        },
        {
            "unique_id": 1791735,
            "unique_uuid": "f49569e3-525e-42bd-a769-869a83caeaf5",
            "origin_unique_id": "7216119496098975019",
            "creation_info": {
                "created_at": "2023-03-29T23:51:49Z",
                "timestamp": "2023-03-29T23:51:49Z"
            },
            "author": {
                "id": 302048,
                "username": "sephora"
            },
            "context": {
                "main_text": "#SephoraSquad member @samtalu has been on a HUNT to find makeup that looks good on camera and in person.",
                "token_count": 19,
                "char_count": 104,
                "tag_count": 2
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@sephora/video/7216119496098975019"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/4b054845-4dbb-4031-b1d5-fac386b0d9b6.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2871,
                        "count": 16800
                    },
                    "views": {
                        "id": 2340,
                        "count": 25300000
                    },
                    "comments": {
                        "id": 2940,
                        "count": 58
                    }
                }
            },
            "author_details": {
                "unique_id": 302048,
                "unique_uuid": "279484737629323264",
                "origin_unique_id": "279484737629323264",
                "info": {
                    "name": "sephora",
                    "platform": "instagram"
                },
                "username": "sephora",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 7402,
                            "count": "931900"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://p16-sign-sg.tiktokcdn.com/aweme/1080x1080/tos-alisg-avt-0068/smg71630d66b7a573be2525c01e74f615fe.jpeg?x-expires=1678014000&x-signature=v0NHfB5gs46Cuhx4I1A0QOHdmjA%3D"
                    ]
                },
                "texts": {
                    "profile_text": "We belong to something beautiful."
                }
            }
        },
        {
            "unique_id": 400391,
            "unique_uuid": "ede90b0a-5bd8-4db1-8268-6251e46aa395",
            "origin_unique_id": "7110626403707653381",
            "creation_info": {
                "created_at": "2022-06-18T17:02:06Z",
                "timestamp": "2022-06-18T17:02:06Z"
            },
            "author": {
                "id": 304770,
                "username": "bessan_esmail"
            },
            "context": {
                "main_text": "١٢ لون بلاشر جديد من بنفت متوفر حصريا في سيفورا😍 #benefitmiddleeast #benefitblush@benefitmiddleeast #sephoramiddleeast #sephora @sephora  #بيسان_اسماعيل #بيسان #دبي #fyp",
                "token_count": 20,
                "char_count": 169,
                "tag_count": 9
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@bessan_esmail/video/7110626403707653381"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/5781f10b-9355-4a4d-a3a0-8d396b33aae2.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2962,
                        "count": 485200
                    },
                    "views": {
                        "id": 2679,
                        "count": 10800000
                    },
                    "comments": {
                        "id": 2750,
                        "count": 5860
                    }
                }
            },
            "author_details": {
                "unique_id": 304770,
                "unique_uuid": "200392870741377024",
                "origin_unique_id": "200392870741377024",
                "info": {
                    "name": "بيسان اسماعيل - Bessan Ismail",
                    "platform": "instagram"
                },
                "username": "bessan_esmail",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 7476,
                            "count": "13600000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        "https://hellozelf.nyc3.cdn.digitaloceanspaces.com/content/4e3924b0-3005-438d-be0f-2b8327eeeb55.jpg"
                    ]
                },
                "texts": {
                    "profile_text": "Syrian Artists🎤\nتواصل:bessanismail@worldofbusiness.agency\nبيتي الجديد😭⬇️"
                }
            }
        },
        {
            "unique_id": 2028860,
            "unique_uuid": "4fc68d40-4e0b-4b41-9425-88517bdb80a2",
            "origin_unique_id": "CrkoXsUL0SF",
            "creation_info": {
                "created_at": "2023-04-28T00:00:00Z",
                "timestamp": "2023-04-28T00:00:00Z"
            },
            "author": {
                "id": 934041,
                "username": "maybelline"
            },
            "context": {
                "main_text": "1 brush, 2 swipes, 3 day wear with our #tattoobrowstlyinggel! AMAZING! With our Maybelline girls @itzy.all.in.us #ITZYPASSTHEPACK",
                "token_count": 17,
                "char_count": 129,
                "tag_count": 3
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/CrkoXsUL0SF"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/36a225b0-1758-447b-a1d0-fdc5202c5182.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2505,
                        "count": 509848
                    },
                    "views": {
                        "id": 2512,
                        "count": 3100000
                    },
                    "comments": {
                        "id": 2659,
                        "count": 888
                    }
                }
            },
            "author_details": {
                "unique_id": 934041,
                "unique_uuid": "ig_maybelline",
                "origin_unique_id": "ig_maybelline",
                "info": {
                    "name": "Maybelline New York",
                    "platform": "instagram"
                },
                "username": "maybelline",
                "stats": {
                    "digg_count": {
                        "followers": {
                            "id": 6721,
                            "count": "11700000"
                        }
                    }
                },
                "avatar": {
                    "urls": [
                        ""
                    ]
                },
                "texts": {
                    "profile_text": "💄Maybe it’s Maybelline💋📍Born in New York🚕🗽🔗 Learn about our mental health initiative Brave Together ⬇️ www.maybelline.com/bravetogether"
                }
            }
        },
        {
            "unique_id": 395772,
            "unique_uuid": "5d60ff21-d7a0-41e3-ab7a-eff69f665895",
            "origin_unique_id": "6967028565388905734",
            "creation_info": {
                "created_at": "2021-05-27T17:49:08Z",
                "timestamp": "2021-05-27T17:49:08Z"
            },
            "author": {
                "id": 302822,
                "username": "lifeoftanyamarie"
            },
            "context": {
                "main_text": "#stitch with @glamzilla woah😂 @patrickstarrr @sephora  #shook #makeupreview #sephora #woah #imshook #foryou #fyp #doesitwork #makeuphack",
                "token_count": 16,
                "char_count": 136,
                "tag_count": 11
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@lifeoftanyamarie/video/6967028565388905734"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/9206823e-349e-47ca-a753-ea9ae707c57e.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2439,
                        "count": 2800000
                    },
                    "views": {
                        "id": 3136,
                        "count": 19000000
                    },
                    "comments": {
                        "id": 2293,
                        "count": 7388
                    }
                }
            }
        },
        {
            "unique_id": 3112971,
            "unique_uuid": "ab7146dd-e9ea-4e06-b6cd-594771866461",
            "origin_unique_id": "7088789357393415429",
            "creation_info": {
                "created_at": "2022-04-20T20:43:10Z",
                "timestamp": "2022-04-20T20:43:10Z"
            },
            "author": {
                "id": 497543,
                "username": "theisleofparadise"
            },
            "context": {
                "main_text": "What’s your fave moisturizer to mix with our Self-Tan Drops? Tell us below👇 #selftan #isleofparadise #sephora #MoveWithTommy #takeaNAIRbreak",
                "token_count": 18,
                "char_count": 140,
                "tag_count": 6
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@theisleofparadise/video/7088789357393415429"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/a74c11a2-e702-4037-95e6-15a9700828e2.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 3047,
                        "count": 150600
                    },
                    "views": {
                        "id": 2501,
                        "count": 10000000
                    },
                    "comments": {
                        "id": 2754,
                        "count": 112
                    }
                }
            }
        },
        {
            "unique_id": 2058093,
            "unique_uuid": "305d189d-0060-457b-84c3-b12528022370",
            "origin_unique_id": "Cr4eQ-Qgnad",
            "creation_info": {
                "created_at": "2023-05-06T00:00:00Z",
                "timestamp": "2023-05-06T00:00:00Z"
            },
            "author": {
                "id": 944019,
                "username": "yurilamasbella"
            },
            "context": {
                "main_text": "POV: when you’re a sister not invited to the Met #relatable #kuwtk #funnyvideos #comedy #kiehlspartner",
                "token_count": 15,
                "char_count": 102,
                "tag_count": 6
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/Cr4eQ-Qgnad"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/a8079b55-3889-48a2-8e51-1a3e2e5ecb61.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 3159,
                        "count": 133921
                    },
                    "views": {
                        "id": 2285,
                        "count": 1700000
                    },
                    "comments": {
                        "id": 3084,
                        "count": 2906
                    }
                }
            }
        },
        {
            "unique_id": 4847822,
            "unique_uuid": "3d9bfbd1-d6ea-41c5-b8ad-61c84fffe4a5",
            "origin_unique_id": "7066001270716304686",
            "creation_info": {
                "created_at": "2022-02-18T10:53:49Z",
                "timestamp": "2022-02-18T10:53:49Z"
            },
            "author": {
                "id": 760311,
                "username": "ideatimes"
            },
            "context": {
                "main_text": "Very satisfying trick💯🔥#viral #satisfying #tipsandtricks #SephoraLipLooks #learnontiktok #hack #relaxing #foryoupage #fypシ",
                "token_count": 11,
                "char_count": 122,
                "tag_count": 10
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@ideatimes/video/7066001270716304686"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/6eb669d1-879b-4b4b-8302-9b0f9c0adc84.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2769,
                        "count": 39600
                    },
                    "views": {
                        "id": 2621,
                        "count": 11400000
                    },
                    "comments": {
                        "id": 2328,
                        "count": 99
                    }
                }
            }
        },
        {
            "unique_id": 2390084,
            "unique_uuid": "6d3cafee-be4c-46f9-9ee8-843378261cc0",
            "origin_unique_id": "CsW9JCJg6A8",
            "creation_info": {
                "created_at": "2023-05-29T00:00:00Z",
                "timestamp": "2023-05-29T00:00:00Z"
            },
            "author": {
                "id": 1056801,
                "username": "sesamestreet"
            },
            "context": {
                "main_text": "Self-care is important. Even just a few minutes of “you time” can help you recharge to be your best. Just ask #OscarTheGrouch! 💚#WellnessWednesday",
                "token_count": 23,
                "char_count": 146,
                "tag_count": 3
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/CsW9JCJg6A8"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/f0caa6e6-d10d-48ac-ad1a-3518f61dbcd2.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2773,
                        "count": 123128
                    },
                    "views": {
                        "id": 2716,
                        "count": 181000
                    },
                    "comments": {
                        "id": 3106,
                        "count": 94
                    }
                }
            }
        },
        {
            "unique_id": 4443913,
            "unique_uuid": "e878abb4-077b-41f3-b4d1-1f302e621806",
            "origin_unique_id": "7262396058905414955",
            "creation_info": {
                "created_at": "2023-08-01T16:45:58Z",
                "timestamp": "2023-08-01T16:45:58Z"
            },
            "author": {
                "id": 297819,
                "username": "sonya_styles"
            },
            "context": {
                "main_text": "On the hunt for drunk elephant goldi drops…✨ #drunkelephant #goldidrops #bronzidrops #drunkelephantbronzedrops #drunkelephantbronzingdrops #drunkelephantbronzer #bronzingdrops #sephora #sephorashopping #viralmakeup #viralproducts #viralmakeupproducts #viralskincare #bestskincare #bestskincareproducts #skincaretok #makeuptok #sephoratok #drunkelephant🐘💗 #comeshoppingwithme #comeshopwithme #aestheticskincare #sephorahaul #sephorahauls #trending ",
                "token_count": 34,
                "char_count": 447,
                "tag_count": 26
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@sonya_styles/video/7262396058905414955"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/6768f4bd-c050-4212-9d13-4f74fb37a2a3.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2784,
                        "count": 1600000
                    },
                    "views": {
                        "id": 2208,
                        "count": 11700000
                    },
                    "comments": {
                        "id": 3129,
                        "count": 3142
                    }
                }
            }
        },
        {
            "unique_id": 2390087,
            "unique_uuid": "f7037231-8c8a-4520-9079-747c1ab394da",
            "origin_unique_id": "CsbWCu9gqL0",
            "creation_info": {
                "created_at": "2023-05-29T00:00:00Z",
                "timestamp": "2023-05-29T00:00:00Z"
            },
            "author": {
                "id": 1056801,
                "username": "sesamestreet"
            },
            "context": {
                "main_text": "Have you stretched and wiggled today? 🐛",
                "token_count": 7,
                "char_count": 39,
                "tag_count": 1
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/CsbWCu9gqL0"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/a2932f24-91f0-4229-af13-2fd09817e00b.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2508,
                        "count": 119156
                    },
                    "views": {
                        "id": 2315,
                        "count": 120000
                    },
                    "comments": {
                        "id": 2921,
                        "count": 0
                    }
                }
            }
        },
        {
            "unique_id": 4841299,
            "unique_uuid": "7bce4cbc-4e94-431f-a391-93309cca3d06",
            "origin_unique_id": "7269817133410913578",
            "creation_info": {
                "created_at": "2023-08-21T16:43:43Z",
                "timestamp": "2023-08-21T16:43:43Z"
            },
            "author": {
                "id": 297819,
                "username": "sonya_styles"
            },
            "context": {
                "main_text": "Stopping at nothing and trying to get my best friend’s dream products and the new sol de jeneiro perfume #soldejeneiro #soldejeneiroafterhours #sdj #sephora #sephorashopping #viralmakeupproducts #viralskincareproducts #viralskincare #viral #trending #sephorahaul #sephorahauls #makeuphaul #sephoratok #makeuptok #skincaretok #skincare #aestheticskincare #aestheticmakeup #makeupessentials #skincareessentials #rarebeautymakeup ",
                "token_count": 42,
                "char_count": 427,
                "tag_count": 23
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@sonya_styles/video/7269817133410913578"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/74f38c90-2273-46b6-af19-57825c59638e.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2488,
                        "count": 1600000
                    },
                    "views": {
                        "id": 3078,
                        "count": 11300000
                    },
                    "comments": {
                        "id": 2719,
                        "count": 2957
                    }
                }
            }
        },
        {
            "unique_id": 2390099,
            "unique_uuid": "4d8bb60c-b109-4e14-a43e-bb6972f26906",
            "origin_unique_id": "Cs7BPOcgF1W",
            "creation_info": {
                "created_at": "2023-05-29T00:00:00Z",
                "timestamp": "2023-05-29T00:00:00Z"
            },
            "author": {
                "id": 1056801,
                "username": "sesamestreet"
            },
            "context": {
                "main_text": "We want to remind you that taking care of yourself doesn’t have to be a chore! Games like “Hear and Seek” are a fun way to reconnect with your mind, body, and surroundings. 💛  Join the fun with @mkbhd and watch the special in our link in story! #ElmosMindfulnessSpectacular #WellnessWednesday #EmotionalWellbeing",
                "token_count": 52,
                "char_count": 312,
                "tag_count": 4
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://instagram.com/p/Cs7BPOcgF1W"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/c06deb6c-273b-43af-83ee-f075d8a44dd9.jpg"
                ],
                "media_type": "IMAGE"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2901,
                        "count": 122667
                    },
                    "views": {
                        "id": 3152,
                        "count": 1200000
                    },
                    "comments": {
                        "id": 2846,
                        "count": 697
                    }
                }
            }
        },
        {
            "unique_id": 1791601,
            "unique_uuid": "853b88be-ab85-42aa-ab72-38328bd511d3",
            "origin_unique_id": "7221972321022528814",
            "creation_info": {
                "created_at": "2023-04-14T18:21:10Z",
                "timestamp": "2023-04-14T18:21:10Z"
            },
            "author": {
                "id": 302048,
                "username": "sephora"
            },
            "context": {
                "main_text": "It’s TIME! Save the dates with #SephoraSquad member @Kristina Rodulfo. Did we mention free shipping for all Beauty Insiders?",
                "token_count": 19,
                "char_count": 124,
                "tag_count": 2
            },
            "origin_details": {
                "origin_platform": "instagram",
                "origin_url": "https://tiktok.com/@sephora/video/7221972321022528814"
            },
            "media": {
                "urls": [
                    "https://nyc3.digitaloceanspaces.com/hellozelf/content/1a18197b-d975-43e7-91c8-7c14f9173354.jpg"
                ],
                "media_type": "VIDEO"
            },
            "stats": {
                "digg_counts": {
                    "likes": {
                        "id": 2533,
                        "count": 122300
                    },
                    "views": {
                        "id": 2741,
                        "count": 66200000
                    },
                    "comments": {
                        "id": 2189,
                        "count": 755
                    }
                }
            }
        }
    ],
    "total_contents": 163,
    "page_size": 30
}
```