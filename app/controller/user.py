import os


class User:
    """
        get user database/relationships
    """
    def __init__(self, user_relationships=os.path.join(os.path.split(os.path.abspath(__file__))[0],
                                                       "data", "user.txt")):
        """Get user relationships from text file

        :param user_relationships:str
        """
        self.user_relationships = user_relationships

    def user_data(self) -> dict:
        """read user.txt file and return data as object

        :return: object
        """
        _users = {}
        with open(self.user_relationships, buffering=1024, encoding='utf-8', mode='r') as _data:
            rows = _data.readlines()
            for row in rows:
                user_info = row.strip().split('follows')
                user_follows = user_info[-1]

                if ',' in user_follows:
                    user_follows = [name.strip() for name in user_follows.split(',')]
                else:
                    user_follows = [user_follows.strip()]

                user_name = user_info[0].strip()
                _users = self.append_users(obj=_users, key=user_name, values=user_follows)

        return _users

    @staticmethod
    def append_users(obj: dict, key: str, values: list) -> dict:
        """

        :param obj: dictionary or entire hashmap
        :param key: string user name
        :param values: list of names followed by user
        :return: dictionary/object
        """
        if key in obj.keys():
            _follows = list(set(values + obj[key]))
            obj[key] = _follows
        else:
            obj[key] = values
        return obj


if __name__ == "__main__":
    user_txt = os.path.join('data', 'user.txt')
    users = User(user_relationships=user_txt).user_data()
    print(users)
