from exts import db
from werkzeug.security import generate_password_hash, check_password_hash


# 员工表
class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # 加上property装饰器后，会把函数变为属性，属性名即为函数
    @property
    def password(self):
        """
        函数的返回值作为属性值，使用property必须要有返回值
        :return:
        """
        raise AttributeError("属性只能设置,不能读取")

    @password.setter
    def password(self, password):
        """
        它在设置属性的时候被调用
        设置属性的方式： user.password = "xxxx"
        :param password: 参数是设置属性的属性值，明文密码
        :return:
        """
        # 在视图中设置user_password属性值时，方法被调用，接收password参数，并将设置为字段值
        self.password = generate_password_hash(password)

    def check_password(self, passwd):
        """
        检验密码的正确性
        :param passwd: 登录时填写的原始密码
        :return: 正确 返回True 错误 返回 False
        """
        return check_password_hash(self.password_hash, passwd)

    def to_dict(self):
        """将对象转换成字典数据"""
        user_dict = {
            "user_id": self.id,
            "username": self.name
        }
        return user_dict
