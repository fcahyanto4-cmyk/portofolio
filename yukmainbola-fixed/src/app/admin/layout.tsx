"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { 
  LayoutDashboard, 
  Users, 
  MapPin, 
  Calendar, 
  Trophy,
  ImageIcon,
  Star,
  Menu,
  X,
  LogOut,
  Globe
} from "lucide-react";

const adminNavs = [
  { name: "Dashboard", href: "/admin", icon: LayoutDashboard },
  { name: "Kelola Pengguna", href: "/admin/users", icon: Users },
  { name: "Kelola Lapangan", href: "/admin/venues", icon: MapPin },
  { name: "Kelola Jadwal", href: "/admin/schedules", icon: Calendar },
  { name: "Event & Turnamen", href: "/admin/events", icon: Trophy },
  { name: "Galeri Foto", href: "/admin/gallery", icon: ImageIcon },
  { name: "Testimoni", href: "/admin/testimonials", icon: Star },
];

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const router = useRouter();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [showLogoutConfirm, setShowLogoutConfirm] = useState(false);

  useEffect(() => {
    const checkAuth = async () => {
      const supabase = createClient();
      const { data: { user } } = await supabase.auth.getUser();
      
      if (!user) {
        router.push("/login?redirectTo=/admin");
        return;
      }

      // Check if user is admin
      const { data: profile } = await supabase
        .from("profiles")
        .select("role")
        .eq("id", user.id)
        .single();

      if (!profile || !["admin", "super_admin"].includes(profile.role)) {
        router.push("/");
        return;
      }

      setUser(user);
      setLoading(false);
    };

    checkAuth();
  }, [router]);

  const handleLogout = async () => {
    setShowLogoutConfirm(true);
  };

  const confirmLogout = async () => {
    const supabase = createClient();
    await supabase.auth.signOut();
    router.push("/");
    router.refresh();
  };

  const cancelLogout = () => {
    setShowLogoutConfirm(false);
  };

  // Close mobile menu on outside click
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (isMobileMenuOpen && !(e.target as Element).closest("aside")) {
        setIsMobileMenuOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, [isMobileMenuOpen]);

  // Close mobile menu on Escape key
  useEffect(() => {
    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === "Escape" && isMobileMenuOpen) {
        setIsMobileMenuOpen(false);
      }
    };
    document.addEventListener("keydown", handleEscape);
    return () => document.removeEventListener("keydown", handleEscape);
  }, [isMobileMenuOpen]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-background">
        <div className="text-center">
          <div className="w-10 h-10 border-4 border-primary border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-text-muted">Memverifikasi akses admin...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return null;
  }

  return (
    <div className="min-h-screen bg-background flex flex-col md:flex-row">
      {/* Logout Confirmation Dialog */}
      {showLogoutConfirm && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
          <div className="bg-surface rounded-xl p-6 border border-border max-w-sm w-full mx-4">
            <h3 className="text-lg font-bold text-text mb-2">Konfirmasi Keluar</h3>
            <p className="text-text-muted mb-4">Apakah Anda yakin ingin keluar dari panel admin?</p>
            <div className="flex gap-2">
              <button
                onClick={cancelLogout}
                className="flex-1 px-4 py-2 rounded-lg border border-border text-text hover:bg-background transition-colors"
              >
                Batal
              </button>
              <button
                onClick={confirmLogout}
                className="flex-1 px-4 py-2 rounded-lg bg-danger text-white hover:bg-danger/90 transition-colors"
              >
                Keluar
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Mobile Header */}
      <div className="md:hidden bg-surface border-b border-border p-4 flex items-center justify-between sticky top-0 z-50">
        <h2 className="text-xl font-bold text-text">Admin Panel</h2>
        <button 
          onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          className="p-2 bg-background rounded-md text-text-muted hover:text-text"
          aria-label={isMobileMenuOpen ? "Tutup menu" : "Buka menu"}
        >
          {isMobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      {/* Sidebar */}
      <aside className={`
        ${isMobileMenuOpen ? 'flex' : 'hidden'} 
        md:flex flex-col w-full md:w-64 bg-surface border-r border-border md:min-h-screen
        fixed md:sticky top-16 md:top-0 z-40 h-[calc(100vh-4rem)] md:h-screen overflow-y-auto
      `}>
        <div className="p-6 hidden md:block">
          <h2 className="text-2xl font-bold text-text">YukMainBola</h2>
          <p className="text-xs text-text-muted uppercase tracking-wider mt-1">Admin Panel</p>
        </div>
        
        <nav className="p-4 space-y-2 flex-1">
          {adminNavs.map((nav) => {
            // FIX: Use startsWith for active nav highlighting
            const isActive = pathname === nav.href || (nav.href !== "/admin" && pathname.startsWith(nav.href));
            const Icon = nav.icon;
            return (
              <Link
                key={nav.href}
                href={nav.href}
                onClick={() => setIsMobileMenuOpen(false)}
                className={`flex items-center gap-3 px-4 py-3 rounded-lg transition-colors font-medium ${
                  isActive 
                    ? "bg-primary text-background" 
                    : "text-text hover:bg-background hover:text-primary"
                }`}
              >
                <Icon size={20} />
                {nav.name}
              </Link>
            );
          })}
        </nav>
        
        <div className="p-4 border-t border-border space-y-2">
          <Link
            href="/"
            className="flex items-center gap-3 px-4 py-3 rounded-lg transition-colors font-medium text-text hover:bg-background hover:text-primary"
          >
            <Globe size={20} />
            Ke Website
          </Link>
          <button
            onClick={handleLogout}
            className="w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-colors font-medium text-danger hover:bg-danger/10"
          >
            <LogOut size={20} />
            Keluar
          </button>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 p-4 md:p-8 w-full">
        {children}
      </main>
    </div>
  );
}
