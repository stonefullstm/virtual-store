error_response_400 = {
                400: {
                    "description": "Validation Error.",
                    "content": {
                        "application/json": {
                            "example": {
                                "message": "Validation error on /name/ field"}
                            }
                    },
                },
             }

error_response_404 = {
                404: {
                    "description": "Not found.",
                    "content": {
                        "application/json": {
                            "example": {
                                "message": "Item not found"}
                            }
                    },
                },
             }
