@RestController
@SpringBootApplication
public class DemoApplication {
    @GetMapping("/")
    public String hello() {
        return "Hello from Spring Boot!";
    }

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}