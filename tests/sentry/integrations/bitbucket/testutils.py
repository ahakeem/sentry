from __future__ import absolute_import

PUSH_EVENT_EXAMPLE = b"""{
    "push": {
        "changes": [
            {
                "links": {
                    "html": {
                        "href": "https://bitbucket.org/maxbittker/newsdiffs/branches/compare/e0e377d186e4f0e937bdb487a23384fe002df649..8f5952f4dcffd7b311181d48eb0394b0cca21410"
                    },
                    "commits": {
                        "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commits?include=e0e377d186e4f0e937bdb487a23384fe002df649&exclude=8f5952f4dcffd7b311181d48eb0394b0cca21410"
                    },
                    "diff": {
                        "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/diff/e0e377d186e4f0e937bdb487a23384fe002df649..8f5952f4dcffd7b311181d48eb0394b0cca21410"
                    }
                },
                "commits": [
                    {
                        "links": {
                            "approve": {
                                "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commit/e0e377d186e4f0e937bdb487a23384fe002df649/approve"
                            },
                            "statuses": {
                                "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commit/e0e377d186e4f0e937bdb487a23384fe002df649/statuses"
                            },
                            "comments": {
                                "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commit/e0e377d186e4f0e937bdb487a23384fe002df649/comments"
                            },
                            "self": {
                                "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commit/e0e377d186e4f0e937bdb487a23384fe002df649"
                            },
                            "patch": {
                                "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/patch/e0e377d186e4f0e937bdb487a23384fe002df649"
                            },
                            "html": {
                                "href": "https://bitbucket.org/maxbittker/newsdiffs/commits/e0e377d186e4f0e937bdb487a23384fe002df649"
                            },
                            "diff": {
                                "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/diff/e0e377d186e4f0e937bdb487a23384fe002df649"
                            }
                        },
                        "date": "2017-05-24T01:05:47+00:00",
                        "hash": "e0e377d186e4f0e937bdb487a23384fe002df649",
                        "parents": [
                            {
                                "type": "commit",
                                "links": {
                                    "html": {
                                        "href": "https://bitbucket.org/maxbittker/newsdiffs/commits/8f5952f4dcffd7b311181d48eb0394b0cca21410"
                                    },
                                    "self": {
                                        "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commit/8f5952f4dcffd7b311181d48eb0394b0cca21410"
                                    }
                                },
                                "hash": "8f5952f4dcffd7b311181d48eb0394b0cca21410"
                            }
                        ],
                        "type": "commit",
                        "message": "README.md edited online with Bitbucket",
                        "author": {
                            "type": "author",
                            "user": {
                                "type": "user",
                                "display_name": "Max Bittker",
                                "uuid": "{b128e0f6-196a-4dde-b72d-f42abc6dc239}",
                                "username": "maxbittker",
                                "links": {
                                    "html": {
                                        "href": "https://bitbucket.org/maxbittker/"
                                    },
                                    "avatar": {
                                        "href": "https://bitbucket.org/account/maxbittker/avatar/32/"
                                    },
                                    "self": {
                                        "href": "https://api.bitbucket.org/2.0/users/maxbittker"
                                    }
                                }
                            },
                            "raw": "Max Bittker <max@getsentry.com>"
                        }
                    }
                ],
                "old": {
                    "type": "branch",
                    "links": {
                        "html": {
                            "href": "https://bitbucket.org/maxbittker/newsdiffs/branch/master"
                        },
                        "commits": {
                            "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commits/master"
                        },
                        "self": {
                            "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/refs/branches/master"
                        }
                    },
                    "target": {
                        "links": {
                            "html": {
                                "href": "https://bitbucket.org/maxbittker/newsdiffs/commits/8f5952f4dcffd7b311181d48eb0394b0cca21410"
                            },
                            "self": {
                                "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commit/8f5952f4dcffd7b311181d48eb0394b0cca21410"
                            }
                        },
                        "date": "2017-05-19T22:53:22+00:00",
                        "hash": "8f5952f4dcffd7b311181d48eb0394b0cca21410",
                        "parents": [
                            {
                                "type": "commit",
                                "links": {
                                    "html": {
                                        "href": "https://bitbucket.org/maxbittker/newsdiffs/commits/1cdfa36e62e615cdc73a1d5fcff1c706965b186d"
                                    },
                                    "self": {
                                        "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commit/1cdfa36e62e615cdc73a1d5fcff1c706965b186d"
                                    }
                                },
                                "hash": "1cdfa36e62e615cdc73a1d5fcff1c706965b186d"
                            }
                        ],
                        "type": "commit",
                        "message": "README.md edited online with Bitbucket",
                        "author": {
                            "type": "author",
                            "raw": "Max Bittker <max@getsentry.com>"
                        }
                    },
                    "name": "master"
                },
                "truncated": false,
                "new": {
                    "type": "branch",
                    "links": {
                        "html": {
                            "href": "https://bitbucket.org/maxbittker/newsdiffs/branch/master"
                        },
                        "commits": {
                            "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commits/master"
                        },
                        "self": {
                            "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/refs/branches/master"
                        }
                    },
                    "target": {
                        "links": {
                            "html": {
                                "href": "https://bitbucket.org/maxbittker/newsdiffs/commits/e0e377d186e4f0e937bdb487a23384fe002df649"
                            },
                            "self": {
                                "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commit/e0e377d186e4f0e937bdb487a23384fe002df649"
                            }
                        },
                        "date": "2017-05-24T01:05:47+00:00",
                        "hash": "e0e377d186e4f0e937bdb487a23384fe002df649",
                        "parents": [
                            {
                                "type": "commit",
                                "links": {
                                    "html": {
                                        "href": "https://bitbucket.org/maxbittker/newsdiffs/commits/8f5952f4dcffd7b311181d48eb0394b0cca21410"
                                    },
                                    "self": {
                                        "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs/commit/8f5952f4dcffd7b311181d48eb0394b0cca21410"
                                    }
                                },
                                "hash": "8f5952f4dcffd7b311181d48eb0394b0cca21410"
                            }
                        ],
                        "type": "commit",
                        "message": "README.md edited online with Bitbucket",
                        "author": {
                            "type": "author",
                            "raw": "Max Bittker <max@getsentry.com>"
                        }
                    },
                    "name": "master"
                },
                "created": false,
                "forced": false,
                "closed": false
            }
        ]
    },
    "repository": {
        "links": {
            "html": {
                "href": "https://bitbucket.org/maxbittker/newsdiffs"
            },
            "avatar": {
                "href": "https://bitbucket.org/maxbittker/newsdiffs/avatar/32/"
            },
            "self": {
                "href": "https://api.bitbucket.org/2.0/repositories/maxbittker/newsdiffs"
            }
        },
        "full_name": "maxbittker/newsdiffs",
        "scm": "git",
        "uuid": "{c78dfb25-7882-4550-97b1-4e0d38f32859}",
        "type": "repository",
        "is_private": false,
        "owner": {
            "type": "user",
            "display_name": "Max Bittker",
            "uuid": "{b128e0f6-196a-4dde-b72d-f42abc6dc239}",
            "username": "maxbittker",
            "links": {
                "html": {
                    "href": "https://bitbucket.org/maxbittker/"
                },
                "avatar": {
                    "href": "https://bitbucket.org/account/maxbittker/avatar/32/"
                },
                "self": {
                    "href": "https://api.bitbucket.org/2.0/users/maxbittker"
                }
            }
        },
        "name": "newsdiffs",
        "website": ""
    },
    "actor": {
        "type": "user",
        "display_name": "Max Bittker",
        "uuid": "{b128e0f6-196a-4dde-b72d-f42abc6dc239}",
        "username": "maxbittker",
        "links": {
            "html": {
                "href": "https://bitbucket.org/maxbittker/"
            },
            "avatar": {
                "href": "https://bitbucket.org/account/maxbittker/avatar/32/"
            },
            "self": {
                "href": "https://api.bitbucket.org/2.0/users/maxbittker"
            }
        }
    }
}
"""
