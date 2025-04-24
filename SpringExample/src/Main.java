public class Main {
    public static void main(String[] args) {
        try {
            // UserDao 인스턴스 생성
            UserDao userDao = new UserDao();

            // 데이터베이스 초기화
            userDao.initializeDatabase();
            System.out.println("Database initialized!");

            // 사용자 추가
            User user = new User();
            user.setId("1");
            user.setName("Alice");
            user.setPassword("password123");

            userDao.add(user);
            System.out.println("User added successfully!");

            // 사용자 조회
            User retrievedUser = userDao.get("1");
            if (retrievedUser != null) {
                System.out.println("Retrieved User: " + retrievedUser.getName());
            } else {
                System.out.println("User not found.");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
